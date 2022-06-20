from dataclasses import fields
import imp
from re import T
from rest_framework import serializers
from blog.models import Article as ArticleModel
from blog.models import Category as CategoryModel
from blog.models import Comment as CommentModel

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ["name"]

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    article = serializers.SerializerMethodField()
    class Meta:
        model = CommentModel
        fields = ["user","comment"]

class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    comments = CommentSerializer(many = True, source = "comment_set")

    def get_comment(self,obj):
        return [category.name for category in obj.category.all()]

    class Meta:
        model = ArticleModel
        fields = ["user", "title", "comments", "category"]