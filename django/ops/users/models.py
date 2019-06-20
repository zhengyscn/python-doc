from django.db import models

# Create your models here.

class Users(models.Model):
    SEX_CHOICES = (
        ('男', '男'),
        ('女', '女'),
        # ('存储的值', '显示的值')
    )

    username    =   models.CharField(max_length=32, unique=True, db_index=True, verbose_name="用户名")
    age         =   models.IntegerField(verbose_name="年龄")
    sex         =   models.CharField(max_length=6, choices=SEX_CHOICES, verbose_name='性别')
    phone       =   models.CharField(max_length=11, unique=True, verbose_name="手机号")
    address     =   models.TextField(blank=True, verbose_name="地址")

    # null=True表示数据库是否唯恐
    # blank=True表示admin是否可提交空值
    remark      =   models.CharField(max_length=200, null=True, blank=True, verbose_name="备注")

    # create_time and update_time只读的， 不允许admin修改.
    create_time =   models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time =   models.DateTimeField(auto_now=True, verbose_name="更新时间")

    '''
    https://blog.51cto.com/xujpxm/2090382
    
    DateTimeField、DateField和TimeField
    其值分别对应着Python里的datetime.datetime、datetime.date和datetime.time三个实例，
    这三个Field里都有两个参数：auto_now和auto_now_add，默认值均为False。
    
    auto_now: 
    每次修改model,都会自动更新
    
    auto_now_add: 
    设置为True时,会在model对象第一次被创建时,将字段的值设置为创建时的时间,以后修改对象时,字段的值不会再更新。
    
    auto_now和auto_now_add被设置为True后,这样做会导致字段成为editable=False和blank=True的状态。
    
    
    blank=Ture表示允许在表单中不输入值
    '''

    class Meta:
        db_table = "users"
        # https://www.cnblogs.com/haoshine/p/6210210.html
        verbose_name = '用户表'
        '''
        verbose_name指定在admin管理界面中显示中文；
        verbose_name表示单数形式的显示，
        verbose_name_plural表示复数形式的显示；中文的单数和复数一般不作区别。
        '''
        verbose_name_plural = verbose_name

        ordering = ['update_time', ]

        # 基类，不生成数据表，只供其它子类来继承
        # abstract = True

        # 设置权限
        # permissions = (('定义好的权限', '权限说明'), )

        # 联合唯一键, 联合唯一约束
        # unique_together = ('username', 'phone')

        # 定义模型类属于哪个application
        # app_label = "users"

        # 定义数据库表空间
        # db_tablespace

    def __str__(self):
        return self.username