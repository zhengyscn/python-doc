from .storage import ImageStorage, BackgroundStorage

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.html import format_html


class Photo(models.Model):
    '''
    照片的数据模型
    '''
    img_upload          = models.ImageField(u'图片上传路径', upload_to='img/%Y/%m/%d', storage=ImageStorage())
    img_title           = models.CharField(max_length=100, unique=True, verbose_name=u'图片标题')
    img_context         = models.TextField(max_length=100, null=True, blank=True, verbose_name=u'图片介绍')
    img_tags            = models.ManyToManyField('Tag', blank=True)
    is_top              = models.BooleanField(u'置顶', default=False)
    img_group           = models.ForeignKey('PhotoGroup', blank=True)
    like_count          = models.IntegerField(u'点赞数', default=0)
    display             = models.BooleanField(default=True, verbose_name=u'显示')
    author              = models.ForeignKey(User, default='admin', verbose_name=u'作者')
    create_time         = models.DateTimeField(u'图片发布时间', auto_now_add=True)
    update_time         = models.DateTimeField(u'图片更新时间', auto_now=True)


    def image_view(self):
        # return u'<img src="%s" height="40"/>' % (settings.MEDIA_URL + str(self.img_upload))
        return format_html(u'<img src="%s" height="40"/>' % (settings.MEDIA_URL + str(self.img_upload)))

    # 页面显示的字段名称
    image_view.short_description = '图片展示'
    image_view.allow_tags = True

    def __str__(self):
        return self.img_title

    class Meta:
        verbose_name = u'照片'
        verbose_name_plural = u'照片'


class Tag(models.Model):
    """
    标签的数据模型
    """
    name                = models.CharField(max_length=20, null=True, blank=True, )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = u'标签'
        verbose_name_plural = u'标签'


class PhotoGroup(models.Model):
    """
    标签的数据模型
    """
    name                = models.CharField(max_length=20, verbose_name=u'相册名')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = u'相册'
        verbose_name_plural = u'相册'



class IndexBackground(models.Model):
    """
    相册背景图片的数据模型
    """
    name = models.CharField(max_length=20, verbose_name=u'背景名')
    img_upload = models.ImageField(u'图片上传路径', upload_to='background', storage=BackgroundStorage())

    def image_view(self):
        return u'<img src="%s" height="500px"/>' % (settings.MEDIA_URL + str(self.img_upload))

    image_view.short_description = '图片展示'
    image_view.allow_tags = True

    class Meta:
        verbose_name = u'背景图片'
        verbose_name_plural = u'背景图片'