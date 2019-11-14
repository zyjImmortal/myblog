from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from blog.utils.models import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=20, verbose_name="文章标题")
    digest = models.CharField(max_length=100, verbose_name="文章摘要")
    image = models.ImageField(verbose_name="封面图")
    content = RichTextUploadingField(default='', verbose_name='文章内容')
    category = models.ForeignKey("categories.Category", on_delete=models.CASCADE,
                                 related_name="category_article", verbose_name="类别")
    # models.CASCADE级联删除，主表中的内容删除时，从表中的数据也要删除
    # comment = models.ForeignKey("comments.Comment", on_delete=models.CASCADE,
    #                             related_name="comment_article", verbose_name="文章评论")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "articles"
        verbose_name = "文章"
        verbose_name_plural = verbose_name
