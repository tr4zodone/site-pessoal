from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError

# Create your models here.

def limit_number_of_instances(obj, INSTANCE_QUANTITY):
    model = obj.__class__
    if (model.objects.count() > (INSTANCE_QUANTITY - 1) and
            obj.id != model.objects.get().id):
        raise ValidationError("Pode-se criar apenas {} instância(s) de: {}".format(INSTANCE_QUANTITY, model.__name__))


class About(models.Model):
    organizing_title = models.CharField(max_length=100)
    body = RichTextUploadingField()

    def __str__(self):
        return self.organizing_title

    def clean(self):
        limit_number_of_instances(self, 1)

    class Meta:
        verbose_name_plural = 'About'

class Index(models.Model):
    organizing_title = models.CharField(max_length=100)
    body = RichTextUploadingField()

    def __str__(self):
        return self.organizing_title

    def clean(self):
        limit_number_of_instances(self, 1)

    class Meta:
        verbose_name_plural = 'Index'


class English(models.Model):
    organizing_title = models.CharField(max_length=100)
    body = RichTextUploadingField()

    def __str__(self):
        return self.organizing_title

    def clean(self):
        limit_number_of_instances(self, 1)

    class Meta:
        verbose_name_plural = 'English'

