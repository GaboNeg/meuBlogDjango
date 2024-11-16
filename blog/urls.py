from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='lista_posts'),  
    path('post/<int:pk>/', PostDetailView.as_view(), name='detalha_post'), 
    path('post/criar/', PostCreateView.as_view(), name='cria_post'), 
    path('post/editar/<int:pk>/', PostUpdateView.as_view(), name='edita_post'),  
    path('post/deletar/<int:pk>/', PostDeleteView.as_view(), name='deleta_post'),
]
