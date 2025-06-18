from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from shop.models import *
from .permission import *

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Items.objects.all()
        name = self.request.query_params.get('name', None)
        decription = self.request.query_params.get('decription', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif decription is not None:
            queryset = queryset.filter(decription__icontains=decription)
        return queryset

        

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Order.objects.all()
        buyer_name = self.request.query_params.get('buyer_name', None)
        buyer_surname = self.request.query_params.get('buyer_surname', None)

        if buyer_name is not None:
            queryset = queryset.filter(buyer_name__icontains=buyer_name)
        elif buyer_surname is not None:
            queryset = queryset.filter(buyer_surname__icontains=buyer_surname)
        return queryset

class Pos_orderViewSet(viewsets.ModelViewSet):
    queryset = Pos_order.objects.all()
    serializer_class = PosOrderSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Pos_order.objects.all()
        items = self.request.query_params.get('items', None)
        order = self.request.query_params.get('order', None)

        if items is not None:
            queryset = queryset.filter(items__icontains=items)
        elif order is not None:
            queryset = queryset.filter(order__icontains=order)
        return queryset

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get('name', None)
        decription = self.request.query_params.get('decription', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif decription is not None:
            queryset = queryset.filter(decription__icontains=decription)
        return queryset

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Collection.objects.all()
        name = self.request.query_params.get('name', None)
        decription = self.request.query_params.get('decription', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif decription is not None:
            queryset = queryset.filter(decription__icontains=decription)
        return queryset

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Customer.objects.all()
        name = self.request.query_params.get('name', None)
        contact_info = self.request.query_params.get('contact_info', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif contact_info is not None:
            queryset = queryset.filter(contact_info__icontains=contact_info)
        return queryset



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Customer.objects.all()
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)

        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)
        elif last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)
        return queryset



class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get('name', None)
        country = self.request.query_params.get('country', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif country is not None:
            queryset = queryset.filter(country__icontains=country)
        return queryset