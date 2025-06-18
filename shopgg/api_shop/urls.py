from .views import *
from rest_framework import routers

urlpatterns = [
]

router = routers.SimpleRouter()
router.register('items', ItemsViewSet, basename='items')
router.register('pos-order', Pos_orderViewSet, basename='pos-order')
router.register('order', OrderViewSet, basename='order')
router.register('collection', CollectionViewSet, basename='collection')
router.register('category', CategoryViewSet, basename='category')
router.register('brand', BrandViewSet, basename='brand')
router.register('supplier', SupplierViewSet, basename='supplier')
urlpatterns += router.urls