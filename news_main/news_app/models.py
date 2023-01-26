from django.db import models
from autoslug import AutoSlugField
# Create your models here.


class Category(models.Model):
    cat = models.CharField(max_length=30)

    def __str__(self):
        return self.cat

    class Meta:
        verbose_name_plural = 'Category'


class NewsPage(models.Model):
    new_cat = models.ForeignKey(
        'Category', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    image = models.ImageField(upload_to="my_image", null=True)
    cat_id = models.IntegerField()
    user_name = models.CharField(max_length=30, null=True)
    time = models.CharField(max_length=50, null=True)
    news_slug = AutoSlugField(populate_from = 'title', unique = True, null = True, default = None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'News'
