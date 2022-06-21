from os import stat
from unicodedata import category
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from Django.permissions import IsAdminOrIsAuthenticatedReadOnly, three_days
from blog.serializers import ArticleSerializer
from datetime import datetime

from .models import Article as ArticleModel

# Create your views here.

class ArticleView(APIView):
    permission_classes = [IsAdminOrIsAuthenticatedReadOnly]

    # def get(self, request):
    #     user = request.user
    #     articles = ArticleModel.objects.filter(user=user)
    #     titles = [article.title for article in articles]

    #     for article in articles:
    #         titles.append(article.title)

    #     return Response({"title": titles})
    def get(self,request):
        today = datetime.now()
        articles = ArticleModel.objects.filter(
            start_date__lte=today,
            end_date__gte=today
        ).order_by('-id')
        
        return Response(ArticleSerializer(articles, many=True).data, status=status.HTTP_200_OK)



    # permission_classes = [three_days]
    def post(self, request):

        user = request.user
        request.data['user'] = user.id
        article_serializer = ArticleSerializer(data=request.data)

        if article_serializer.is_valid():
            article_serializer.save()
            return Response(article_serializer.data, status=status.HTTP_200_OK)
            
        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        # #---------------------------------------------------------------
        # #기본적인 posting 방법입니다 !!
        
        # user = request.user
        # title = request.data.get('title', '')
        # categories = request.data.get('category', '')
        # contents = request.data.get('content', '')

        # if len(title) <= 5:
        #     return Response({"message": "제목이 5글자 이하입니다."})
        # if len(contents)<=20:
        #     return Response({"message": "내용은 20글자 이하입니다."})
        # if category is None:
        #     return Response({"message": "카테고리를 지정해야 합니다."})
        
        # article = ArticleModel.objects.create(user=user, **request.data)
        # article.category.add(*categories)
        # article.save()
        # return Response({"message" : "게시물 생성!"})
        # #-----------------------------------------------------------------