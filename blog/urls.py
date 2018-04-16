from django.urls import path, re_path, include
from . import views

urlpatterns = [
    #root
    path("", views.blog_top_view, name="blog"),

    #detail
    re_path("posts/(?P<pk>\d+)/(?P<slug>[-\w]+)/$", views.PostDetailView.as_view(), name="post_detail"),

    # criar
    path(r'posts/create/new/', views.NovoPost.as_view(), name='novo_post'),

    # ver rascunhos e potencialmente publicar
    re_path(r'^posts/rascunhos/$', views.rascunhos, name='rascunhos'),
    re_path(r'^posts/rascunhos/(?P<slug>[-\w]+),(?P<pk>\d+)/$', views.publicar_post, name='publicar_post'),

    # editar e remover
    re_path(r'^posts/editar/(?P<slug>[-\w]+),(?P<pk>\d+)/$', views.AtualizarPost.as_view(), name='post_edit'),
    re_path(r'^posts/remover/(?P<slug>[-\w]+),(?P<pk>\d+)/$', views.Remover_Post.as_view(), name='remover'),

    # ckeditor
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
