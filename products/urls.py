from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('novo/', views.product_create, name='product_create'),
    path('<int:pk>/editar/', views.product_edit, name='product_edit'),
    path('<int:pk>/deletar/', views.product_delete, name='product_delete'),
    path('<int:pk>/adicionar-estoque/', views.product_add_stock, name='product_add_stock'),
    path('<int:pk>/remover-estoque/', views.product_remove_stock, name='product_remove_stock'),
]
