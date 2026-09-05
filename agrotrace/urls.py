from django.urls import path
from . import views

app_name = 'agrotrace'

urlpatterns = [
    # Fundos
    path('fundos/', views.fundo_list, name='fundo_list'),
    path('fundos/nuevo/', views.fundo_create, name='fundo_create'),
    path('fundos/editar/<int:pk>/', views.fundo_update, name='fundo_update'),
    path('fundos/eliminar/<int:pk>/', views.fundo_delete, name='fundo_delete'),

    # Lotes
    path('lotes/', views.lote_list, name='lote_list'),
    path('lotes/nuevo/', views.lote_create, name='lote_create'),
    path('lotes/editar/<int:pk>/', views.lote_update, name='lote_update'),
    path('lotes/eliminar/<int:pk>/', views.lote_delete, name='lote_delete'),
]