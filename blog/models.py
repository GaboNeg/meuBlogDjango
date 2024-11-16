from django.db import models
from django.conf import settings


class Category(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Category, related_name='posts')

    def __str__(self):
        return self.titulo


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usando AUTH_USER_MODEL
    texto = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.autor.username} em {self.post.titulo}'

    class Meta:
        ordering = ['-data_postagem']