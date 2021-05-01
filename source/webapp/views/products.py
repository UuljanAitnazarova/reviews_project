from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductsView(ListView):
    model = Product
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 4
    paginate_orphans = 1


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'

    def get_success_url(self):
        return reverse('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/update.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})