from django.contrib import admin

from .models import Resource, Category, Channel
# Register your models here.


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_filter = ["name", "category"]
    list_display = ["name", "url","category"] 
    list_editable = ["category"]

    view_on_site = False

admin.site.register(Channel)
admin.site.register(Category)
