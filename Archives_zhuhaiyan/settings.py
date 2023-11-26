import os.path
import sys
from pathlib import Path

# 移除文件上传数量的限制
DATA_UPLOAD_MAX_NUMBER_FILES = None

""" 
对于数据库，使用一个特定的路径变量 DATABASE_DIR
判断是否在一个打包环境中
因为单个文件需要在运行时解压到临时目录 """
'''
打包语法(在manage.py的根目录中) pyinstaller --name=Archives_zhuhaiyan --onefile --add-data "archives_app;archives_app" --add-data "Archives_zhuhaiyan;Archives_zhuhaiyan" --add-data "static;static" --add-data "templates;templates" --add-data "S:\\LibreOfficePortable\\App\\libreoffice\\program;LibreOfficePortable\\App\\libreoffice\\program" manage.py
'''
if getattr(sys, 'frozen', False):
    # 如果是，那么路径是 .exe 文件所在的目录
    DATABASE_DIR = Path(os.path.dirname(sys.executable))  #运行的是.exe文件
else:
    # 如果不是，则使用 __file__ 的常规方法
    DATABASE_DIR = Path(__file__).resolve().parent.parent #运行的是python文件

# 对于其他路径，继续使用 BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# 设置 MEDIA_ROOT 为项目根目录下的 'files' 子目录 （存储上传的非文本文件）
MEDIA_ROOT = os.path.join(DATABASE_DIR, 'files')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hnbnd3n5wcet9g$*p!)u4p0r9(rl_wfy-3(xawtdh9lfykq1w7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'archives_app',# 注册新创建的应用app，否则app下的models.py写类（表）时，无法在数据库中创建
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', # 不需要包含 {% csrf_token %} 模板标签来提供 CSRF 令牌
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Archives_zhuhaiyan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 指定模板文件的路径，设置为项目根目录下的 templates 目录
        'DIRS': [os.path.join(BASE_DIR,'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Archives_zhuhaiyan.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# 使用 sqlite3 数据库，避免在打包后的程序中需要安装数据库
# 运行在别人的代码中，不需要安装数据库，直接运行即可
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DATABASE_DIR / "db.sqlite3",
    }
}
# 查看数据库路径（因为没用系统自带的BASE_DIR）
print(f"DATABASE_DIR is set to: {DATABASE_DIR}")

# 原本是利用MySQL数据库，需要MySQL配置进本地环境变量，并设定同USER和PASSWORD和HOST
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': "archives_2022_12_16",
#         'HOST':'127.0.0.1',
#         'PORT':3306,
#         'USER':'root',
#         'PASSWORD':'root'
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# 设置语言为中文
LANGUAGE_CODE = 'zh-hans'

# 设置时区为中国上海
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
