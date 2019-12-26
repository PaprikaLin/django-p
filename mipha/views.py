from django.shortcuts import render, get_object_or_404, get_list_or_404, reverse, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.
from .models import Post
from django.template import loader


# index函数用来获取所有文章，获取到post_lists里面并通过HTTPResponse输出到客户端页面中
def index(request):
    posts = Post.objects.all()
    #post_lists = list()
    #template = loader.get_template('mipha/index.html')
    context = {'posts': posts}
    '''
    硬编码。最好把html和python代码区分开来，使用render函数
    for count, post in enumerate(posts):
        # post_lists.append("No.{}:".format(str(count)) + str(post) + "<br>")
        post_lists.append("No.{}: {} {} {} <br>".format(str(count), str(post.author), str(post), str(post.pub_date)))
    return HttpResponse(post_lists)
    return render(posts, 'template/index.html')
    
    '''

    # render函数 (request, 模板路径 templates/mipha/index.html, 要传递的参数)
    # return render(request, 'mipha/index.html', context)
    return render(request, 'mipha/mainpage.html', context)


# 定义链接应该返回的数据
# 一般做以下几件事
#   1. 从数据库获取数据
#   2. 逻辑判断或者其他需要的事情
#   3. 渲染模板，并且传递参数（目前看来是以字典的键与HTML里面的 {{ }}对应）
def author_poets(request, author):
    # poets = Post.objects.filter(author=author)
    poets = get_list_or_404(Post, author=author)
    context = {'author': author, 'poets': poets}
    return render(request, 'mipha/author_filter.html', context)


def poet_page(request, author, slug):
    poet = get_object_or_404(Post, author=author, slug=slug)
    return render(request, 'mipha/poet.html', {'poet': poet})


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
        if Post.objects.get(title=poet_title):
            return render(request, 'mipha/mainpage.html', {
                'error_message': '这是一个错误信息：这首诗已存在'
            })
        Post.objects.create(title=poet_title, slug=the_slug, author=poet_author, body=poet_body)
        # reverse 相当于通过模板名称倒推出对应的路径，比如说/form/对应formtest模板
        # 那么reverse('mipha:formtest')就会返回/form/

        # 重定向，提交数据要用重定向，防止后退之后重新提交表单
        return HttpResponseRedirect(reverse('mipha:author_poets', args=('李白',)))





