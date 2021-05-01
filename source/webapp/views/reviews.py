from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.models import Review, Product
from webapp.forms import ReviewForm


class ReviewCreateView(CreateView):
    model = Review
    template_name = 'review/create.html'
    form_class = ReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()
        return redirect(reverse('product_detail', kwargs={'pk': product.pk}))


class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'review/update.html'
    form_class = ReviewForm
    context_object_name = 'review'

    def get_success_url(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        return reverse('product_detail', kwargs={'pk': product.pk})


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/delete.html'
    context_object_name = 'review'

    def get_success_url(self):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        return reverse('product_detail', kwargs={'pk': product.pk})
