from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView

from adminapp.forms import UserAdminEditForm, ProductEditForm, CategoryEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import Category, Product


class AccessMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser


class UserCreateView(AccessMixin, CreateView):
    model = ShopUser
    template_name = 'adminapp/user_form.html'
    form_class = ShopUserRegisterForm

    def get_success_url(self):
        return reverse('adminapp:user_read')


class UserListView(AccessMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/user_list.html'
    paginate_by = 2


class UserUpdateView(AccessMixin, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_form.html'
    form_class = UserAdminEditForm

    def get_success_url(self):
        return reverse('adminapp:user_update', args=[self.kwargs.get('pk')])


class UserDeleteView(AccessMixin, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete_confirm.html'

    def get_success_url(self):
        return reverse('adminapp:user_read')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryCreateView(AccessMixin, CreateView):
    model = Category
    # form_class = CategoryEditForm
    fields = ('name', 'description',)
    success_url = reverse_lazy('adminapp:category_read')
    template_name = 'adminapp/category_create.html'


class CategoryListView(AccessMixin, ListView):
    model = Category
    template_name = 'adminapp/category_list.html'


class CategoryUpdateView(AccessMixin, UpdateView):
    model = Category
    template_name = 'adminapp/category_create.html'
    form_class = CategoryEditForm

    def get_success_url(self):
        return reverse('adminapp:category_read')


class CategoryDeleteView(AccessMixin, DeleteView):
    model = Category
    template_name = 'adminapp/category_delete_confirm.html'

    def get_success_url(self):
        return reverse('adminapp:category_read')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# class ProductListView(ListView):
#     model = Product
#     template_name = 'adminapp/products_list.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context_data = super().get_context_data(*args, **kwargs)
#         context_data['category'] = get_object_or_404(Category, pk=self.kwargs.get('pk'))
#         return context_data
#
#     def get_queryset(self):
#         return super().get_queryset().filter(category_id=self.kwargs.get('pk'))


class CategoryDetailView(AccessMixin, DetailView):
    model = Category
    template_name = 'adminapp/products_list.html'


# @user_passes_test(lambda u: u.is_superuser)
# def product_create(request, pk):
#     category_item = get_object_or_404(Category, pk=pk)
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_item = product_form.save()
#             return HttpResponseRedirect(reverse('adminapp:products_read', args=[product_item.category_id]))
#     else:
#         product_form = ProductEditForm()
#     context = {
#         'form': product_form
#     }
#     return render(request, 'adminapp/product_form.html', context)

class ProductCreateView(AccessMixin, CreateView):
    model = Product
    template_name = 'adminapp/product_form.html'
    form_class = ProductEditForm

    def get_success_url(self):
        category_pk = self.get_object().category_id
        return reverse('adminapp:products_read')


@user_passes_test(lambda u: u.is_superuser)
def products_update(request):
    return None


class ProductDeleteView(AccessMixin, DeleteView):
    model = Product
    template_name = 'adminapp/product_confirm_delete.html'

    def get_success_url(self):
        category_pk = self.get_object().category_id
        return reverse('adminapp:products_read', args=[category_pk])

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ProductDetailView(AccessMixin, DetailView):
    model = Product
    template_name = 'adminapp/product_info.html'
