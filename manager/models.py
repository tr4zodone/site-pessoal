from django.db import models

# Create your models here.

class Channel(models.Model):
    initials = models.CharField(max_length=10, blank=False, unique=True)  

    def __str__(self):
        return self.initials

class Category(models.Model):
    title = models.CharField(max_length=120, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"

class Resource(models.Model):
    name = models.CharField(max_length=120, blank=False) 
    url = models.URLField(blank=False) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name



