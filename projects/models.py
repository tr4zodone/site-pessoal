from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Project(models.Model):
    abstract = True
    title = models.CharField(max_length=120, blank=False, unique=True)
    description = models.TextField(max_length=240, null=True,blank=True, unique=False)

    def __str__(self):
        return self.title

class Website(Project):
    url = models.URLField(blank=False, unique=True)

class ArtAlbum(Project):
    slug = models.SlugField(max_length=100, blank=True)
    cover = models.ImageField(upload_to="media", null=True) 

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(ArtAlbum, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts_per_category", kwargs={'slug':self.slug})


class ArtObject(models.Model):
    album = models.ForeignKey(ArtAlbum, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=120, blank=False, unique=True)
    image = models.ImageField(upload_to="media")

    def __str__(self):
        return self.title
