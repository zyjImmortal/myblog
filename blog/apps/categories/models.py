from django.db import models

# Create your models here.
from blog.utils.models import BaseModel


class Category(BaseModel):

    name = models.CharField(max_length=10,verbose_name="类别名称")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"
        verbose_name = "分类"
        verbose_name_plural = verbose_name