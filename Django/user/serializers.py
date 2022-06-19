from dataclasses import fields
import imp
from rest_framework import serializers

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ["comment"]

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ["user", "title"]

class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    
    def get_same_hobby_users(self, obj): #obj의 값은 아래에 Meta에 선언한 HobbyModel이 된다.
        # user_list = []
        # for user_profile in obj.userprofile_set.all():
        #     user_list.append(user_profile.user.username)

        return [up.user.username for up in obj.userprofile_set.all()]

    class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many = True)
    #여기에 objects로 들어오는지, 아니면 queryset으로 들어오는지를 알아야 함
    #queryset으로 들어 오려면 (many=True가 필요)
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age", "hobby"]


class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article = ArticleSerializer()
    comment = CommentSerializer()
    class Meta:
        model = UserModel
        fields = ["username", "email", "fullname", "join_data", "userprofile", "article", "comment"] #모델에서 가져올 수 있는 값, 역참조 가능