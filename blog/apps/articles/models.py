from django.db import models

# Create your models here.
from blog.utils.models import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=20, verbose_name="文章标题")
    summary = models.CharField(max_length=100,verbose_name="文章摘要")


    def __str__(self):
        return self.title