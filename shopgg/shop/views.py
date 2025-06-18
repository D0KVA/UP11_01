from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from .models import *
from .forms import *
from basket.forms import BasketAddProductForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin



def general_view(request):
    return render(request, 'general.html')

def company_view(request):
    return render(request, 'company.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def places_view(request):
    return render(request, 'places.html')

def items_view(request):
    return render(request, 'items.html')

def category_view(request):
    return render(request, 'category.html')

def all_view(request):
    return render(request, 'all.html')

def basket_view(request):
    return render(request, 'basket.html')

class ItemsListView(ListView):
    model = Items
    template_name = 'items/items_list.html'
    context_object_name = 'items'

class ItemsDetailView(DetailView):
    model = Items
    template_name = 'items/items_detail.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context

class ItemsCreateView(PermissionRequiredMixin ,CreateView):
    permission_required='shop.add_item'
    model = Items
    form_class = ItemsForm
    template_name = 'items/items_form.html'
    success_url= reverse_lazy('product_list_view')

class ItemsUpdateView(UpdateView):
    model = Items
    form_class = ItemsForm
    template_name = 'items/items_form.html'
    success_url= reverse_lazy('product_list_view')

class ItemsDeleteView(DeleteView):
    model = Items
    template_name = 'items/items_confirm_delete.html'
    success_url= reverse_lazy('product_list_view')


class SuppliersListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_supplier'
    model = Supplier
    template_name = 'suppliers/suppliers_list.html'
    context_object_name = 'supplier'

class SuppliersDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_supplier'
    model = Supplier
    template_name = 'suppliers/suppliers_detail.html'
    context_object_name = 'supplier'

class SuppliersCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_supplier'
    model = Supplier
    form_class = SuppliersForm
    template_name = 'suppliers/suppliers_form.html'
    success_url = reverse_lazy('suppliers_list_view')

class SuppliersUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_supplier'
    model = Supplier
    form_class = SuppliersForm
    template_name = 'suppliers/suppliers_form.html'
    success_url = reverse_lazy('suppliers_list_view')

class SuppliersDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_supplier'
    model = Supplier
    template_name = 'suppliers/suppliers_confirm_delete.html'
    success_url = reverse_lazy('suppliers_list_view')


class BrandsListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_brand'
    model = Brand
    template_name = 'brands/brands_list.html'
    context_object_name = 'brand'

class BrandsDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_brand'
    model = Brand
    template_name = 'brands/brands_detail.html'
    context_object_name = 'brand'

class BrandsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_brand'
    model = Brand
    form_class = BrandsForm
    template_name = 'brands/brands_form.html'
    success_url = reverse_lazy('brands_list_view')

class BrandsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_brand'
    model = Brand
    form_class = BrandsForm
    template_name = 'brands/brands_form.html'
    success_url = reverse_lazy('brands_list_view')

class BrandsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_brand'
    model = Brand
    template_name = 'brands/brands_confirm_delete.html'
    success_url = reverse_lazy('brands_list_view')


class CategoriesListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_category'
    model = Category
    template_name = 'categories/categories_list.html'
    context_object_name = 'category'

class CategoriesDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_category'
    model = Category
    template_name = 'categories/categories_detail.html'
    context_object_name = 'category'

class CategoriesCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_category'
    model = Category
    form_class = CategoriesForm
    template_name = 'categories/categories_form.html'
    success_url = reverse_lazy('categories_list_view')

class CategoriesUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_category'
    model = Category
    form_class = CategoriesForm
    template_name = 'categories/categories_form.html'
    success_url = reverse_lazy('categories_list_view')

class CategoriesDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_category'
    model = Category
    template_name = 'categories/categories_confirm_delete.html'
    success_url = reverse_lazy('categories_list_view')


class CollectionsListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_collection'
    model = Collection
    template_name = 'collections/collections_list.html'
    context_object_name = 'collection'

class CollectionsDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_collection'
    model = Collection
    template_name = 'collections/collections_detail.html'
    context_object_name = 'collection'

class CollectionsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_collection'
    model = Collection
    form_class = CollectionsForm
    template_name = 'collections/collections_form.html'
    success_url = reverse_lazy('collections_list_view')

class CollectionsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_collection'
    model = Collection
    form_class = CollectionsForm
    template_name = 'collections/collections_form.html'
    success_url = reverse_lazy('collections_list_view')

class CollectionsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_collection'
    model = Collection
    template_name = 'collections/collections_confirm_delete.html'
    success_url = reverse_lazy('collections_list_view')


class CustomersListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_customer'
    model = Customer
    template_name = 'customers/customers_list.html'
    context_object_name = 'customer'

class CustomersDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_customer'
    model = Customer
    template_name = 'customers/customers_detail.html'
    context_object_name = 'customer'

class CustomersCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_customer'
    model = Customer
    form_class = CustomersForm
    template_name = 'customers/customers_form.html'
    success_url = reverse_lazy('customers_list_view')

class CustomersUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_customer'
    model = Customer
    form_class = CustomersForm
    template_name = 'customers/customers_form.html'
    success_url = reverse_lazy('customers_list_view')

class CustomersDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_customer'
    model = Customer
    template_name = 'customers/customers_confirm_delete.html'
    success_url = reverse_lazy('customers_list_view')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('product_list_view')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', context={'form': form})

def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('product_list_view')
    else:
        form = RegistrationForm()
    return render(request, 'auth/registration.html', context={'form': form})

def logout_user(request):
    logout(request)
    return redirect('product_list_view')