from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=30,verbose_name='类别名称')
    def __str__(self):
        return '<Category:%s>'%self.cname
    class Meta:
        verbose_name_plural = '类别'

class Tag(models.Model):
    tname = models.CharField(max_length=30,verbose_name='标签名称')

    def __str__(self):
        return '<Tag:%s>'%self.tname
    class Meta:
        verbose_name_plural = '标签'
from ckeditor_uploader.fields import RichTextUploadingField
class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    desc = models.CharField(max_length=100,verbose_name='描述')
    content = RichTextUploadingField(verbose_name='内容')
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,verbose_name='类别名称')
    tag = models.ManyToManyField(Tag,verbose_name='标签')

    def __str__(self):
        return '<Post:%s>'%self.title
    class Meta:
        verbose_name_plural = '帖子'