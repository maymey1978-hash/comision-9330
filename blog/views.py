from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'blog/lista_posts.html', {'posts': posts})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post': post})

@login_required
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

@login_required
def editar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/crear_post.html', {'form': form, 'es_edicion': True})

@login_required
def eliminar_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')
    return render(request, 'blog/confirmar_eliminar.html', {'post': post})
