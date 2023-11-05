from .models import Product, ProductImage, ProductReview
from .serializers import ProductSerializer, ProductImageSerializer, ProductReviewSerializer

def common_create(data, serializer_class):
    serializer = serializer_class(data=data)
    if serializer.is_valid():
        serializer.save()
        return{'success': True, 'message': 'Item added successfully', 'data': serializer.data}
    return{'success':False, 'message': 'Item creation failed', 'errors': serializer.errors}

def common_update(instance, data, serializer_class):
    serializer = serializer_class(instance, data=data)
    if serializer.is_valid():
        serializer.save()
        return {'success': True, 'message': 'Item updated successfully', 'data': serializer.data}
    return {'success': False, 'message': 'Item update failed', 'errors': serializer.errors}

def common_delete(instance):
    try:
        instance.delete()
        return {'success': True, 'message': 'Item deleted successfully'}
    except Exception as e:
        return {'success': False, 'message': f'Item deletion failed: {str(e)}'}

def common_get(queryset, serializer_class, many=True):
    serializer = serializer_class(queryset, many=many)
    return {'success': True, 'data': serializer.data}

def common_get_single(instance, serializer_class):
    serializer = serializer_class(instance)
    return {'success': True, 'data': serializer.data}