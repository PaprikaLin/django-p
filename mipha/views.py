from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.
from .models import Post
from django.template import loader
from django.views import generic

'''
# index函数用来获取所有文章，获取到post_lists里面并通过HTTPResponse输出到客户端页面中
def index(request):
    posts = Post.objects.all()
    #post_lists = list()
    #template = loader.get_template('mipha/index.html')
    context = {'posts': posts}

    # 硬编码。最好把html和python代码区分开来，使用render函数
    # for count, post in enumerate(posts):
    #     # post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
    #     post_lists.append("No.{}: {} {} {} <br>".format(str(count), str(post.author), str(post), str(post.pub_date)))
    # return HttpResponse(post_lists)
    # return render(posts, 'template/index.html')


    # render函数 (request, 模板路径 templates/mipha/index.html, 要传递的参数)
    # return render(request, 'mipha/index.html', context)
    return render(request, 'mipha/mainpage.html', context)
'''

class IndexView(generic.ListView):
    model = Post
    # 继承自ListView, 所以自动生成的变量是  post_list
    # 如果需要修改，通过 context_object_name 属性
    template_name = 'mipha/mainpage.html'


    def get_queryset(self):
        # 应该是用来读取数据库的函数
        return Post.objects.order_by('-pub_date')


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
        print('queryset   ',self.kwargs)
        return Post.objects.filter(author=self.kwargs['author'], slug=self.kwargs['slug'])


def formtest(request):
    '''try:
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
        Post.objects.create(title=poet_title, slug=the_slug, author=poet_author, body=poet_body)
        # reverse 相当于通过模板名称倒推出对应的路径，比如说/form/对应formtest模板
        # 那么reverse('mipha:formtest')就会返回/form/

        # 重定向，提交数据要用重定向，防止后退之后重新提交表单'''
    return HttpResponseRedirect(reverse('mipha:author_poets', args=('李白',)))





