from django.contrib import admin
from .models import Post
# Register your models here.
# models 里面定义的模型，需要在这里面进行注册
# 注册后应该需要python manage.py migrate更新数据库 ？


# 自定义Post的显示方式，把其他字段也显示进去
# 继承自admin.ModelAdmin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')


# 把新的类也注册进去
admin.site.register(Post, PostAdmin)
