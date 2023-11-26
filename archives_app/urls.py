from django.urls import path
from archives_app import views

'''
列表urlpatterns包含了 URL 模式和视图函数的映射关系
name 参数就是为了在模板templates中引用特定的 URL 模式
<form action="{% url 'archives_generate_view' %}"
'''

urlpatterns = [
    
    # 处理用户直接访问网站根URL的情况
    path('', views.home, {'pages': 1}, name='home_view'),
    # 使用尖括号和转换器来捕获页码
    path('home/<int:pages>/', views.home, name='home_view'),
    # 编辑功能
    path('archives_edit/<int:edit_id>/edit/', views.archives_edit, name='archives_edit_view'),
    # 删除功能
    path('archives_delete/<int:delete_id>/', views.archives_delete, name='archives_delete_view'),
    # 生成所有档案的属性（包含上传文件和文件夹）
    path('archives_generate/', views.archives_generate, name='archives_generate_view'),
    # 删除所有档案
    path('delete_all/', views.delete_all, name='delete_all_view'),
    # 下载到本地
    path('archives_download/<int:id>/', views.archives_download, name='archives_download_view'),
    # 数据库导出到本地
    path('archives_export/', views.archives_export, name='archives_export'),
    # 数据可视化
    path('archives_visualization/', views.archives_visualization, name='archives_visualization_view'),
    # 添加一个新的路径，指向 GPT-3.5 对话视图

]
