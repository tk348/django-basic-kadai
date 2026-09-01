from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .models import Product


class TopView(TemplateView):
    template_name = "top.html"


class ProductListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("product_list")


class ProductDetailView(DetailView):
    model = Product
