from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Category')

    def __str__(self):
        return self.name


class System(models.Model):
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=256, verbose_name='Operating system')
    logo = models.ImageField(upload_to='./static/images/', null=True, blank=True, verbose_name='Official Logo')

    def __str__(self):
        return self.name
