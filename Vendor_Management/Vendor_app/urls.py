from django.urls import path
from .views import (
    VendorListCreateView,
    VendorRetrieveUpdateDestroyView,
    PurchaseOrderListCreateView,
    PurchaseOrderRetrieveUpdateDestroyView,
    VendorPerformanceView,
)

urlpatterns = [

    path('vendors/', VendorListCreateView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroyView.as_view(), name='vendor-detail'),
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-order-detail'),
    path('vendors/<int:pk>/performance/', VendorPerformanceView.as_view(), name='vendor-performance')

]