from django.contrib import admin
from django.urls import path

from crud.views import (
    TopView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductDetailView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", TopView.as_view(), name="top"),

    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),

    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]