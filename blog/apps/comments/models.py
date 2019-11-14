from django.db import models

# Create your models here.
from blog.utils.models import BaseModel


class Comment(BaseModel):
    content = models.CharField(max_length=100, verbose_name="评论内容")
    article = models.ForeignKey("articles.Article", on_delete=models.CASCADE,
                                verbose_name="文章", related_name="article_comment")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name="父级评论", null=True, blank=True)

    class Meta:
        db_table = "comments"
        verbose_name = "评论"
        verbose_name_plural = verbose_name
