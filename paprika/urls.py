"""paprika URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mipha import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('mipha/', include('mipha.urls'))
    # 这里include了mipha.urls那么所有mipha/urls.py里面定义的路径，都要以这个为前缀
    # 比如这里如果定义的是 "polls/"那么实际路径都要是 "polls/1" 这样的。
    path('', include('mipha.urls')),
]
