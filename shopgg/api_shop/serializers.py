from rest_framework import serializers
from shop.models import Category, Collection, Items, Supplier, Order, Pos_order, Brand, Customer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            'name',
            'description'
        ]

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'name',
            'country'
        ]

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'contact_info',
            'photo'
        ]

class ItemSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=10, decimal_places=2)
    class Meta:
        model = Items
        fields = [
            'name',
            'description',
            'price',
            'photo',
            'create_date',
            'is_exists',
            'category',
            'collection',
            'brand',
            'supplier'
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'buyer_firstname',
            'buyer_name',
            'buyer_surname',
            'comment',
            'delivery_addresses',
            'delivery_type',
            'date_create',
            'date_finish',
            'items'
        ]

class PosOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pos_order
        fields = [
            'items',
            'order',
            'count',
            'discount'
        ]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone'
        ]