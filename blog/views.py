from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})


def detalha_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detalha_post.html', {'post': post})


def cria_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        post = Post.objects.create(titulo=titulo, conteudo=conteudo)
        return redirect('detalha_post', post_id=post.id)
    return render(request, 'blog/cria_post.html')


def edita_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.titulo = request.POST.get('titulo')
        post.conteudo = request.POST.get('conteudo')
        post.save()
        return redirect('detalha_post', post_id=post.id)
    return render(request, 'blog/edita_post.html', {'post': post})


def deleta_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'blog/deleta_post.html', {'post': post})


