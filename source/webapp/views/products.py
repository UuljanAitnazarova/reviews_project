from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from webapp.forms import ProductForm
from webapp.models import Product, Review


class ProductsView(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 4
    paginate_orphans = 1


class ProductReviewsView(ListView):
    template_name = 'product/detail.html'
    paginate_by = 2
    paginate_orphans = 1
    context_object_name = 'reviews'

    def get_queryset(self):
        self.product = get_object_or_404(Product, pk=self.kwargs['pk'])
        return Review.objects.filter(product=self.product)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.product
        return context


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product/create.html'
    form_class = ProductForm
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('product_list')


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/delete.html'
    permission_required = 'webapp.delete_product'

    def get_success_url(self):
        return reverse('product_list')


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})