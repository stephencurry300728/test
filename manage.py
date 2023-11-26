import os
import sys
import threading
import time
import socket
import webbrowser
from django.core.management import execute_from_command_line, call_command
from django.db.utils import OperationalError
import django

def is_port_open(host, port):
    """检查指定的端口是否开放（即服务器是否就绪）"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(2)  # 设置超时时间
        result = sock.connect_ex((host, port))
        return result == 0

def open_browser():
    """在服务器启动后自动打开浏览器"""
    while not is_port_open("127.0.0.1", 8000):
        print("等待服务器启动...")
        time.sleep(1)  # 每次检查之间等待1秒
    webbrowser.open('http://127.0.0.1:8000/')  # 使用默认的网页浏览器打开指定的URL

def check_migrations_and_apply():
    """检查并应用数据库迁移"""
    # 定义数据库文件的路径
    # 在打包后，该数据库应该与打包出的 .exe 文件位于同一目录下。
    db_path = 'db.sqlite3'
    
    # 检查数据库文件是否存在。
    if not os.path.exists(db_path):
        # 如果不存在，打印提示信息并执行迁移命令。
        print("数据库不存在，将执行迁移。")
        # 调用 Django 的管理命令来执行迁移操作，interactive=False 表示在执行时不与用户交互。
        call_command('migrate', interactive=False)
    else:
        try:
            # 尝试从 archives_app 应用的 models 模块导入 Archives 模型。
            from archives_app.models import Archives
            # 检查 Archives 模型对应的数据库表是否存在。
            # 如果下面的语句执行无误，则证明表存在，不需要进行迁移。
            Archives.objects.exists()
        except OperationalError as e:
            # 如果抛出 OperationalError 异常，进一步检查异常信息。
            if 'no such table' in str(e):
                # 如果异常信息中包含 'no such table'，说明表不存在，需要执行迁移。
                call_command('migrate', interactive=False)
                # 执行迁移后打印提示信息。
                print("数据库迁移已执行。")
            else:
                # 如果抛出的异常不是由于表不存在引起的，则重新抛出该异常，
                # 让异常可以在控制台中显示，以便进行进一步的调试。
                raise


if __name__ == "__main__":
    '''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings') 这行代码用于设置环境变量 DJANGO_SETTINGS_MODULE
    它告诉 Django 项目的设置文件位于哪里 'djangoProject.settings' 应该指向你的项目(Project)的设置文件
    比如 myproject为项目名称 那么应设定 'myproject.settings' 这样 Django 才能正确地找到并使用你的设置文件
    '''
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Archives_zhuhaiyan.settings")
    # 初始化Django
    django.setup()
    # 检查并应用数据库迁移
    check_migrations_and_apply()

    # 启动服务器的逻辑
    if len(sys.argv) == 1:
        sys.argv.extend(["runserver", "--noreload"])
        # 开始监听服务器是否启动，如果启动了再打开浏览器，免得出现浏览器打开了但是服务器没启动的情况
        threading.Thread(target=open_browser).start()

    # Run A ManagementUtility.
    execute_from_command_line(sys.argv)
