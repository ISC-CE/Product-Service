from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Product, ProductImage, ProductReview
from .serializers import ProductSerializer, ProductImageSerializer, ProductReviewSerializer
from django.contrib import messages
from django.http import JsonResponse

from .common_functions import common_create, common_update, common_delete, common_get, common_get_single


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        result = common_create(data, ProductSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        result = common_update(instance, data, ProductSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        #data = request.data()
        result = common_delete(instance)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message}, status=204)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        result = common_get(queryset, ProductSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        result = common_get_single(instance, ProductSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        result = common_create(data, ProductImageSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        result = common_update(instance, data, ProductImageSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        result = common_delete(instance, data, ProductImageSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message}, status=204)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        result = common_get(queryset, ProductImageSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        result = common_get_single(instance, ProductImageSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

'''class ProductInventoryViewSet(viewsets.ModelViewSet):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer'''

class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        result = common_create(data, ProductReviewSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        result = common_update(instance, data, ProductReviewSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        result = common_delete(instance)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        result = common_get(queryset, ProductReviewSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        result = common_get_single(instance, ProductReviewSerializer)
        message = result.get('message', '')
        if result['success']:
            return JsonResponse({'message': message, 'data': result['data']}, status=200)
        return JsonResponse({'error': message, 'errors': result['errors']}, status=400)