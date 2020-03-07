from django.contrib import admin

from .models import Resource, Category, Channel
# Register your models here.

admin.site.register(Resource)
admin.site.register(Channel)
admin.site.register(Category)
