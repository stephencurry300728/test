"""Archives_zhuhaiyan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include


'''
这里使用了Including another URLconf的方法, 即包含另一个URLconf
include('archives_app.urls')的作用是告诉Django
当用户访问网站根URL时,应该参考archives_app应用内部的urls.py文件中定义的URL模式。
'''
urlpatterns = [
    # 空页面留给archives_app应用的urls.py处理
    path('', include('archives_app.urls')), 
    # Django自带的管理员界面，其实这里没用到
    path('admin/', admin.site.urls),
]