from django.db import models

# Create your models here.
from blog.utils.models import BaseModel


class Comment(BaseModel):

    content = models.CharField(max_length=100, verbose_name="评论内容")


    class Meta:
        db_table = "comments"
        verbose_name = "评论"
        verbose_name_plural = verbose_name