from django.urls import path

from webapp.views import (
    ProductsView,
    ProductReviewsView,
    ProductCreateView,
    ProductDeleteView,
    ProductUpdateView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
)

urlpatterns = [
    path('', ProductsView.as_view(), name='product_list'),
    path('<int:pk>', ProductReviewsView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/reviews/create', ReviewCreateView.as_view(), name='review_create'),
    path('reviews/<int:pk>/update', ReviewUpdateView.as_view(), name='review_update'),
    path('reviews/<int:pk>/delete', ReviewDeleteView.as_view(), name='review_delete'),
]