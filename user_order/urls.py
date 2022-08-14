from django.urls import path

from .views import ShopViewSet, OrderViewSet

urlpatterns = [
    path('shop', ShopViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('shop/<str:pk>', ShopViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destory',
    })),
     
    path('order', OrderViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
     path('order/<str:pk>', OrderViewSet.as_view({
        'get': 'retrieve',
        'patch': 'update',
        'delete': 'destory',
    })),
]
