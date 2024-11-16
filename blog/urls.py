from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:post_id>/', views.detalha_post, name='detalha_post'),
    path('criar/', views.cria_post, name='cria_post'),
    path('editar/<int:post_id>/', views.edita_post, name='edita_post'),
    path('deletar/<int:post_id>/', views.deleta_post, name='deleta_post'),
]
