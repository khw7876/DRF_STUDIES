from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Article as ArticleModel

# Create your views here.

class ArticleView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        articles = ArticleModel.objects.filter(user=user)

        titles = [article.title for article in articles]
        

        for article in articles:
            titles.append(article.title)

        return Response({"title": titles})