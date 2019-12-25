from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
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
    poets = Post.objects.filter(author=author)
    # poets = get_object_or_404(Post, author=author) get方法只能返回一个对象，多个对象不适用
    context = {'author': author, 'poets': poets}
    return render(request, 'mipha/author_filter.html', context)


def poets(request, author, slug):
    poet = get_object_or_404(Post, author=author, slug=slug)
    return render(request, 'mipha/poet.html', {'poet': poet})


