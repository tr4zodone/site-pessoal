from django.db import models
from django.db.models import signals
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# update slugs automatically
def instance_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.title)

# Create your models here.
class Tag(models.Model):
    slug = models.SlugField(max_length=100, blank=True, default="")
    title = models.CharField(max_length=90, blank=False, unique=True,
                              error_messages={'unique':"Essa tag ja existe"})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts_per_category", kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    signals.pre_save.connect(instance_pre_save, sender="blog.Tag")

class Post(models.Model):
    title = models.CharField(max_length=120, unique=True, error_messages={'unique': "Voce ja criou uma postagem com esse titulo"})
    content = RichTextUploadingField() 
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=120, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk, 'slug':self.slug})

    def article_pre_save(signal, instance, sender, **kwargs):
        instance.slug = slugify(instance.title)

    signals.pre_save.connect(article_pre_save, sender="blog.Post")
