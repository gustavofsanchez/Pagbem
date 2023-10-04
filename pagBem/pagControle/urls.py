from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('deletar_cliente/<str:pk>/', views.deletar_cliente, name='deletar_cliente'),
    path('editar_cliente/<str:pk>/', views.editar_cliente, name='editar_cliente'),
    path('editar_cliente_modal/<str:pk>/', views.editar_cliente_modal, name='editar_cliente_modal'),
]
