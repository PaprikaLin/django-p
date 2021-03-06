from django.contrib import admin
from .models import Post, Blog
# Register your models here.
# models 里面定义的模型，需要在这里面进行注册
# 注册后应该需要python manage.py migrate更新数据库 ？


# 自定义Post的显示方式，把其他字段也显示进去
# 继承自admin.ModelAdmin
class PostAdmin(admin.ModelAdmin):
    list_display = ('body', 'pub_date', 'author', 'visible', 'ip_addr', 'mail', 'id')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'pub_date', 'body', 'read')


# 把新的类也注册进去
admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
