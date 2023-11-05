"""
URL configuration for ecommerce_product_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.urls import path
from ProductService import api_views  # Import your API views module

from rest_framework import routers
from ProductService.api_views import ProductViewSet, ProductImageViewSet, ProductReviewViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
#router.register(r'inventory', ProductInventoryViewSet)
router.register(r'images', ProductImageViewSet)
router.register(r'reviews', ProductReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/Product/', api_views.ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-api-endpoint'),
    path('api/Product', api_views.ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-api-endpoint'),
    path('api/Product/<int:pk>/', api_views.ProductViewSet.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}), name='product-api-endpoint'),
    path('api/Product/<int:pk>', api_views.ProductViewSet.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}), name='product-api-endpoint'),
    #path('api/ProductInventory/', api_views.ProductInventoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_inventory-api-endpoint'),
    path('api/ProductImage/', api_views.ProductImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_image-api-endpoint'),
    path('api/ProductImage', api_views.ProductImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_image-api-endpoint'),
    path('api/ProductImage/<int:pk>/', api_views.ProductImageViewSet.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}), name='product_image-api-endpoint'),
    path('api/ProductImage/<int:pk>', api_views.ProductImageViewSet.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}), name='product_image-api-endpoint'),
    path('api/ProductReview/', api_views.ProductReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_review-api-endpoint'),
    path('api/ProductReview/<int:pk>/', api_views.ProductReviewViewSet.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}), name='product_review-api-endpoint'),
    path('api/ProductReview', api_views.ProductReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_review-api-endpoint'),
    path('api/ProductReview/<int:pk>', api_views.ProductReviewViewSet.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}), name='product_review-api-endpoint'),
]   

'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/Product/', api_views.ProductViewSet.as_view(), name='product-api-endpoint'),
    path('api/Product/<int:pk>/', api_views.ProductViewSet.as_view(), name='product-api-endpoint'),
    #path('api/ProductInventory/', api_views.ProductInventoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_inventory-api-endpoint'),
    path('api/ProductImage/', api_views.ProductImageViewSet.as_view(), name='product_image-api-endpoint'),
    path('api/ProductImage/<int:pk>/', api_views.ProductImageViewSet.as_view(), name='product_image-api-endpoint'),
    path('api/ProductReview/', api_views.ProductReviewViewSet.as_view(), name='product_review-api-endpoint'),
    path('api/ProductReview/<int:pk>/', api_views.ProductReviewViewSet.as_view(), name='product_review-api-endpoint'),
]   '''



