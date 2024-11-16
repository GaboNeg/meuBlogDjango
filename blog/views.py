from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})


def detalha_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detalha_post.html', {'post': post})


def cria_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista_posts')
    else:
        form = PostForm()

    return render(request, 'blog/cria_post.html', {'form': form})


def edita_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalha_post', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edita_post.html', {'form': form, 'post': post})


def deleta_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'blog/deleta_post.html', {'post': post})


