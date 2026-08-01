from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('post/nuevo/', views.crear_post, name='crear_post'),
]
