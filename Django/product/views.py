import imp
from urllib import request
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from blog.models import Article as ArticleModel
from user.models import User as UserModel

from blog.serializers import ArticleSerializer

from datetime import datetime
from Django.permissions import IsAdminOrIsAuthenticatedReadOnly

from product.serializers import ProductSerializer
from product.models import Product as ProductModel

from django.db.models import Q
# Create your views here.

class ProductView(APIView):
    # 상품 조회
    def get(self, request):
        today = datetime.now()
        products = ProductModel.objects.filter(
            Q(exposure_start_date__lte=today, exposure_end_date__gte=today, ) | 
            Q(user=request.user)
        )
        return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)
    
    
    # 상품 등록
    def post(self, request):
        request.data['user'] = request.user.id
        product_serializer = ProductSerializer(data=request.data)
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # 상품 수정
    def put(self, request, obj_id):
        product = ProductModel.objects.get(id=obj_id)
        product_serializer = ProductSerializer(product, data=request.data, partial=True)
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    # 상품 삭제
    def delete(self, request,obj_id):
        pass
        # request.data['user'] = request.user.id
        # product = ProductModel.objects.get(name=obj_id)
        # product_serializer = ProductSerializer(product, data=request.data, partial=True)
        # product_serializer.delete()
        # return Response(product_serializer.data, status=status.HTTP_200_OK)
    