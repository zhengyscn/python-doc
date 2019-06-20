from django.db import models

# Create your models here.


class Teacher(models.Model):
    '''
        讲师信息表
    '''
    username        =   models.CharField(max_length=32, primary_key=True, db_index=True, verbose_name="用户名")
    intro           =   models.TextField(default="这个人很懒，什么都没留下.", verbose_name='简介')
    create_at       =   models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at       =   models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'teacher'
        verbose_name = "讲师信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Course(models.Model):
    '''
        课表表
        课表 和 讲师 是 一对多
    '''
    TYPE_CHOICE = (
        (1, 'Python训练营'),
        (2, 'Python自动化'),
        (3, 'Go实战班'),
        (4, 'Docker+K8s'),
    )
    title           =   models.CharField(max_length=100, primary_key=True, db_index=True, verbose_name="课程名")

    # 删除级联
    teacher         =   models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE, verbose_name='课程讲师')
    type            =   models.IntegerField(choices=TYPE_CHOICE, max_length=1, verbose_name='课程类型')
    create_at       =   models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at       =   models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'course'
        verbose_name = "课表表"
        verbose_name_plural = verbose_name

    def __str__(self):
        # return '{} - {}'.format(self.get_type_display(), self.title)
        return f'{self.get_type_display()} - {self.title}'


class Student(models.Model):
    '''
        学生表
        学生 和 课程 是 多 对多
    '''
    SEX_CHOICE = (
        (1, '男'),
        (2, '女'),
    )
    username        =   models.CharField(max_length=100, primary_key=True, db_index=True, verbose_name="课程名")
    age             =   models.IntegerField(verbose_name="年龄")
    sex             =   models.CharField(choices=SEX_CHOICE, max_length=1, verbose_name='性别')
    course          =   models.ManyToManyField(Course, verbose_name="别名")
    create_at       =   models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at       =   models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'student'
        verbose_name = "学生表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username



class TeacherAssistant(models.Model):
    '''
        助教信息表
    '''
    SEX_CHOICE = (
        (1, '男'),
        (2, '女'),
    )
    username        =   models.CharField(max_length=32, primary_key=True, db_index=True, verbose_name="用户名")
    love            =   models.TextField(null=True, blank=True, verbose_name="爱好")
    teacher         =   models.OneToOneField(Teacher, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='讲师')
    create_at       =   models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at       =   models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "teacher_assistant"
        verbose_name = "助教信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username