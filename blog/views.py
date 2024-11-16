from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



class PostListView(ListView):
    model = Post
    template_name = 'blog/lista_posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detalha_post.html'
    context_object_name = 'post'

    def get_object(self):
        post = super().get_object()
        if not post:
            raise Http404("Post não encontrado")
        return post
    

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/cria_post.html'
    success_url = reverse_lazy('lista_posts')


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/edita_post.html'
    success_url = reverse_lazy('lista_posts')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/deleta_post.html'
    success_url = reverse_lazy('lista_posts')


def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.autor = request.user
            comment.save()
            return redirect('detalha_post', pk=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/detalha_post.html', {'post': post, 'form': form})