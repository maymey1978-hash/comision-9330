from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

# Vista para ver todas las publicaciones
def lista_posts(request):
    posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'blog/lista_posts.html', {'posts': posts})

# Vista para ver un post en detalle
def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post': post})

# Vista para crear una nueva publicación
@login_required
def crear_post(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        subtitulo = request.POST.get('subtitulo')
        cuerpo = request.POST.get('cuerpo')
        imagen = request.FILES.get('imagen')
        
        Post.objects.create(
            titulo=titulo,
            subtitulo=subtitulo,
            cuerpo=cuerpo,
            imagen=imagen,
            autor=request.user
        )
        return redirect('lista_posts')
        
    return render(request, 'blog/crear_post.html')
