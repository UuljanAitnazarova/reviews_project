from django.urls import path

from webapp.views import (
    ProductsView,
    ProductDetailView,
    ProductCreateView,
    ProductDeleteView,
    ProductUpdateView,
)

urlpatterns = [
    path('', ProductsView.as_view(), name='product_list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]