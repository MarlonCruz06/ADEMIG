from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_movimentacoes, name='lista_movimentacoes'),
    path('nova/', views.nova_movimentacao, name='nova_movimentacao'),
    path('editar/<int:id>/', views.editar_movimentacao, name='editar_movimentacao'),
    path('excluir/<int:id>/', views.excluir_movimentacao, name='excluir_movimentacao'),
    path('relatorios/', views.relatorios_financeiros, name='relatorios_financeiros'),
]