from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
# Create your views here.
from .models import Post, Likes_record, Comment, Visitor_record
from django.template import loader
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
import markdown
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import requests
from django.utils import timezone
import io

# index函数用来获取所有文章，获取到post_lists里面并通过HTTPResponse输出到客户端页面中
def index(request):
    print(timezone.now().date())
    print(request.session.items())
    posts = Post.objects.all()
    paginator = Paginator(posts, 20)
    post_list = paginator.page(1)
    context = {'post_list': post_list}

    print(request.environ.get('HTTP_USER_AGENT'))
    a = request.environ.get('HTTP_USER_AGENT')
    if ('Mobile' in a) or ('iPhone' in a) or ('Android' in a):
        print('return mobile')
        #return render(request, 'mipha/mobile_index.html', {'post_list': post_list})
        return HttpResponseRedirect(reverse('mipha:mobile_index'), {'post_list': post_list})

    return render(request, 'mipha/mainpage.html', {'post_list': post_list})
    #return render(request, 'mipha/backupmain.html', context)


def page_view(request, page):
    posts = Post.objects.all()
    paginator = Paginator(posts, 20)  # 每页5个对象
    try:
        post_list = paginator.page(page)  # 获取第几页的内容
    except InvalidPage:
        post_list = paginator.page(1)
    context = {'post_list': post_list}
    return render(request, 'mipha/mainpage.html', context)


def post_view(request, page_num):
    post = get_object_or_404(Post, id=page_num)
    # post.body = markdown.markdown(post.body,
    #                               extentions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ])
    return render(request, 'mipha/post.html', {'post': post})


def comment_form(request):
    if request.META.get('REQUEST_METHOD') == 'GET':
        return HttpResponse('Method Not Allowed')
    try:
        # 如果值为空就报错
        post_author = request.POST.get('author')
        post_email =request.POST.get('email')
        print(post_email)
        post_body = request.POST.get('body')
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
    except KeyError:
        # 错误信息，返回提交页面，并且输出一个错误信息
        return render(request, 'mipha/mainpage.html', {
            'error_message': '这是一个错误信息：空值'
        })
    else:
        Post.objects.create(
            author=post_author,
            mail=post_email,
            body=post_body,
            ip_addr=ip)
    visitor_record(request)
    return HttpResponseRedirect(
        reverse('mipha:index'), {'message': 'content'})


def mobile_index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 20)
    post_list = paginator.page(1)
    context = {'post_list': post_list}
    a = request.environ.get('HTTP_USER_AGENT')
    if 'mobile' or 'iPhone' in a:
        print('mobile')
    return render(request, 'mipha/mobile_index.html', {'post_list': post_list})

@csrf_exempt
def increase_like_or_unlike(request):
    # 获取POST过来的信息，在做js的时候要跟这里接口对上
    post_id = request.POST.get('post_id')
    comment_type = request.POST.get('comment_type')
    userip = request.META.get('REMOTE_ADDR')
    post = Post.objects.get(id=post_id)
    res = {'status':0, 'msg':''}
    try:
        new_like = Likes_record.objects.get(post_id=post_id, user=userip)
        res['msg'] = '您已经投过票了'
    except ObjectDoesNotExist:
        if comment_type == '1':
            post.likes += 1
            post.save()
            Likes_record.objects.create(
                post_id=post_id,
                comment_type=1,
                user=userip,)
            res['status'] = 1
            res['msg'] = post.likes
            return JsonResponse(res)
        else:
            post.unlikes += 1
            post.save()
            Likes_record.objects.create(
                post_id=post_id,
                comment_type=0,
                user=userip,)
            res['status'] = 1
            res['msg'] = post.unlikes
        return JsonResponse(res)
    return JsonResponse(res)


def updates_page(request):
    return render(request, 'mipha/updatelog.html')

@csrf_exempt
def upload(request):
    print(request.POST)
    file = request.FILES.get('f1').file.getvalue()

    with open('static/mipha/images/temp.jpg', 'wb') as f:
        f.write(file)
    f1 = {'file': open('static/mipha/images/temp.jpg', 'rb')}
    url = 'https://pic.suo.dog/api/tc.php?type=1688&echo=imgurl'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Referer': 'https://pic.suo.dog/'
    }
    res = requests.post(url, headers=headers, files=f1)
    visitor_record(request)
    return HttpResponse(res.text)



@csrf_exempt
def api_upload(request):

    di = {
        'author': request.POST.get('author'),
        'email': request.POST.get('email'),
        'content': request.POST.get('content'),
    }

    with open('D:/test.jpg', 'wb') as f:
        f.write(bytes(request.POST.get('content'), encoding='utf-8'))
    d = {}
    d['file'] = open('D:/test.jpg', 'rb')
    url = 'https://pic.suo.dog/api/tc.php?type=1688&echo=imgurl'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Referer': 'https://pic.suo.dog/'
    }
    res = requests.post(url, headers=headers, files=d)
    visitor_record(request)
    return HttpResponse(res.text)



@csrf_exempt
def new_comment(request):
    if request.META.get('REQUEST_METHOD') == 'GET':
        return HttpResponse('Method Not Allowed')
    try:
        author = request.POST.get('author')
        post_id = request.POST.get('post_id')
        email = request.POST.get('email')
        content = request.POST.get('content')
        ipaddr = request.META.get('REMOTE_ADDR')
        print(author, post_id, email, content)
    except:
        return HttpResponse('unknown error')
    Comment.objects.create(
        post_id=post_id,
        author=author,
        mail=email,
        content=content,
        ipaddr = ipaddr,
    )
    res = {'status': 1, 'author': author, 'post_id': post_id, 'email': email, 'content': content, 'date': timezone.now().strftime('%Y-%m-%d %H:%M:%S')}
    visitor_record(request)
    return JsonResponse(res)


def get_comment(request, post_id):
    postid = Comment.objects.filter(post_id=post_id)
    comments = {}
    for n, p in enumerate(postid):
        comments[str(n)] = {
            'comment_date': p.pub_date.strftime('%Y-%m-%d %H:%M:%S'),
            'comment_content': p.content,
            'comment_post_id': p.post_id,
            'comment_author': p.author
        }
    data = {'code': 0,
            'comments': comments,
            }
    print(data)
    return JsonResponse(data)




def visitor_record(request):
    m = request.META
    ip = m.get('REMOTE_ADDR')
    agent = m.get('HTTP_USER_AGENT')
    refer = m.get('HTTP_REFERER')
    Visitor_record.objects.create(
        ipaddr=ip,
        user_agent=agent,
        referer=refer
    )
    return None

# class IndexView(generic.ListView):
#     model = Post
#     # 继承自ListView, 所以自动生成的变量是  post_list
#     # 如果需要修改，通过 context_object_name 属性
#     template_name = 'mipha/mainpage.html'
#     context_object_name = 'post_list'
#
#     def get_queryset(self):
#         # 应该是用来读取数据库的函数
#         posts = Post.objects.order_by('-pub_date')
#         paginator = Paginator(posts, 5)
#
#         #page = self.get('page')
#         #return Post.objects.order_by('-pub_date')
#         return paginator.get_page(1)


# 定义链接应该返回的数据
# 一般做以下几件事
#   1. 从数据库获取数据
#   2. 逻辑判断或者其他需要的事情
#   3. 渲染模板，并且传递参数（目前看来是以字典的键与HTML里面的 {{ }}对应）
# def author_poets(request, author):
#     # poets = Post.objects.filter(author=author)
#     poets = get_list_or_404(Post, author=author)
#     context = {'author': author, 'poets': poets}
#     return render(request, 'mipha/author_filter.html', context)
'''
class AuthorPoetsView(generic.ListView):
    model = Post
    template_name = 'mipha/author_filter.html'
    context_object_name = 'poets'

    # 从请求路径中获取参数的方法  self.kwargs
    # self.kwargs 是一个列表，键是在app/urls.py里面定义的路径的名称，这里是author
    # 值是实际的输入，被<str:author>获取到的 "王维"
    def get_queryset(self):
        self.poets = get_list_or_404(Post, author=self.kwargs['author'])
        # context = {'poets': Post.objects.filter(author=self.kwargs['author']), 'author':self.kwargs['author']}
        return Post.objects.filter(author=self.kwargs['author'])

    # 如果要传递额外的参数，要使用get_context_data函数
    # 先通过super取出父类中的 上下文 也就是所有参数——可以看context的打印内容——然后再覆盖或者增加内容
    def get_context_data(self, *, object_list=None, **kwargs):
        print(self.kwargs)
        context = super().get_context_data()
        context['author'] = self.kwargs['author']
        return context

# def poet_page(request, author, slug):
#     poet = get_object_or_404(Post, author=author, slug=slug)
#     return render(request, 'mipha/poet.html', {'poet': poet})


class PoetView(generic.DetailView):
    model = Post
    template_name = 'mipha/poet.html'

    # def get_context_data(self, **kwargs):
    #     print('context  ', self.kwargs)
    #     context = super().get_context_data()
    #     print(context)
    #     print(self.object)
    #     return context

    def get_queryset(self):
        print('queryset   ', self.kwargs)
        return Post.objects.filter(
            author=self.kwargs['author'],
            slug=self.kwargs['slug'])


def formtest(request):
    try:
         # 如果值为空就报错
        poet_title = request.POST['title']
        poet_author = request.POST['author']
        poet_body = request.POST['body']
    except KeyError:
        # 错误信息，返回提交页面，并且输出一个错误信息
        return render(request, 'mipha/mainpage.html', {
            'error_message': '这是一个错误信息：空值'
        })
    else:
        # 操作数据库，增加数据
        the_slug = Post.objects.filter(author=poet_author).count()
        try:
            a = Post.objects.filter(title=poet_title)
        except Post.DoseNotExsit:
            return render(request, 'mipha/mainpage.html', {
                'error_message': '这是一个错误信息：这首诗已存在'
            })
        Post.objects.create(
            title=poet_title,
            slug=the_slug,
            author=poet_author,
            body=poet_body)
        # reverse 相当于通过模板名称倒推出对应的路径，比如说/form/对应formtest模板
        # 那么reverse('mipha:formtest')就会返回/form/

        # 重定向，提交数据要用重定向，防止后退之后重新提交表单

    return HttpResponseRedirect(
        reverse(
            'mipha:author_poets',
            args=(
                poet_author,
            )))
'''
