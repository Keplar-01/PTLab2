from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('buy/<int:product_id>/', views.PurchaseCreate.as_view(), name='buy'),
]
