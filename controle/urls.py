from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('itens/novo/', views.novo_item, name='novo_item'),
    path('itens/<int:id>/editar/', views.editar_item, name='editar_item'),
    path('movimentacao/', views.movimentacao, name='movimentacao'),
]