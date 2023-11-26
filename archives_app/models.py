from django.db import models

# Create your models here.
# The name of each Field instance (e.g. num or name) is the field’s name, 即tables中的字段名, in machine-friendly format. 
# You’ll use this value in your Python code, and your database will use it as the column name（表的列名）

'''
每次对数据库进行更改（新增表或者修改表字段命名或者修改字段的属性等）都需要执行以下命令：

1. python manage.py makemigrations 
在本地创建临时文件运行 makemigrations 命令会让 Django 检查你的模型定义与当前数据库结构之间的差异
并且创建一个新的迁移文件(migration file) 这个文件是一个 Python 脚本，它包含了必须应用到数据库的所有改动的记录
这就是所谓的“创建迁移(migrations)

2. python manage.py migrate 
最后，需要将这些迁移应用到实际的数据库中。当你运行 migrate 命令时Django 会查看所有还没有被应用的迁移文件
并且按照它们创建的顺序执行它们，更新数据库结构，同时尽量不影响现有的数据
'''

class Archives(models.Model):
    id = models.AutoField(primary_key=True)
    # verbose_name 是一个人类可读的字段名，用于表单的 label 标签在模板中直接调用
    num = models.IntegerField(verbose_name='案例编号')
    name = models.CharField(verbose_name='名称', max_length=199)
    line = models.CharField(verbose_name='线路', max_length=599)
    station = models.CharField(verbose_name='车站', max_length=69)
    theme = models.CharField(verbose_name='主题', max_length=69)
    characteristic = models.TextField(verbose_name='特色',max_length=599)
    effect = models.TextField(verbose_name='成效', max_length=599)
    fileName = models.CharField(verbose_name='文件名',max_length=199)

    '''
    数据库中的表名由应用的名称和模型的类名组成，格式是 <应用名>_<模型类名>
    定义 Meta 内部类，直接设置 db_table 属性为 Archives 即数据库中生成表的名称为 Archives 
    '''

    class Meta:
            db_table = 'Archives'
    '''
    renames the instances of the model 当需要把 Archives 的实例对象输出
    使用 '档案名称:' 加上该实例的 name 字段的值
    这意味着每当打印一个 Archives 对象或者在 Django 管理后台查看一个 Archives 对象的时候
    将看到如 "档案名称:某个档案" 的形式，而不是默认的 <Archives object (id)>

    在没有 __str__ 方法的情况下，如果尝试打印 Archives 的一个实例，将会得到如 <Archives object (1)> 的对象结果
    '''
    def __str__(self):
        return f'档案名称:{self.name}'
