from django.urls import path, include
from app import views

urlpatterns = [
    path("start/", views.start, name="Initialize DB"),
    path("category/", views.CategoryListView.as_view(), name="show-categories"),
    path("category/<int:cat_id>", views.CategoryItemView.as_view(), name="show-category-products"),
    path("category/<int:cat_id>/products", views.CategoryProductView.as_view(), name="show-category-products"),
    path("products/", views.ProductListView.as_view(), name="show-categories"),
    path("products/<int:prod_id>", views.ProductItemView.as_view(), name="show-product"),
    path("images/", views.ImageListView.as_view(), name="show-images"),
    path("images/<int:prod_id>", views.ImageProductView.as_view(), name="show-product-images"),
    path("variants/", views.VariantListView.as_view(), name="show-variants"),
    path("variants/<int:prod_id>", views.VariantProductView.as_view(), name="show-product-variants"),
    path("variant-data/", views.VariantDataListView.as_view(), name="show-sizes-of-variants"),
    path("variant-data/<int:var_id>", views.VariantDataVariantView.as_view(), name="show-variant-sizes"),
]