from django import forms
from blog.models import Post, Tag
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from ckeditor_uploader.fields import RichTextUploadingField

class PostForm(forms.ModelForm):

    title = forms.CharField(label="Título")
    content = RichTextUploadingField()

    class Meta():
        model = Post
        fields = ('title', 'tag', 'content')

class TagBuild(forms.ModelForm):
    title = forms.CharField(required=True, label="Nome da tag")

    class Meta():
        model = Tag
        fields = ('title',)
