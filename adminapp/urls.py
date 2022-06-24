from django.urls import path
from adminapp import views as adminapp


app_name = 'adminapp'


urlpatterns = [
    path('users/create/', adminapp.UserCreateView.as_view(), name='user_create'),
    path('users/read/', adminapp.UserListView.as_view(), name='user_read'),
    path('users/update/<pk>/', adminapp.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<pk>/', adminapp.UserDeleteView.as_view(), name='user_delete'),

    path('categories/create', adminapp.CategoryCreateView.as_view(), name='category_create'),
    path('categories/read', adminapp.CategoryListView.as_view(), name='category_read'),
    path('categories/update/<pk>/', adminapp.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<pk>/', adminapp.CategoryDeleteView.as_view(), name='category_delete'),


    path('categories/products/read/<pk>/', adminapp.CategoryDetailView.as_view(), name='products_read'),
    path('products/create/<pk>/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/update/<pk>/', adminapp.products_update, name='products_update'),
    path('products/delete/<pk>/', adminapp.ProductDeleteView.as_view(), name='products_delete'),
    path('products/detail/<pk>/', adminapp.ProductDetailView.as_view(), name='products_detail'),
]
