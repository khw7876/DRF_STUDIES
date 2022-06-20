from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.db.models import F, Q
from django.contrib.auth import authenticate, login, logout

from user.serializers import UserSerializer

from Django.permissions import RegistedMoreThanAWeekUser

from user.models import UserProfile as UserProfileModel
from user.models import User as UserModel
from user.models import Hobby as HobbyMOdel
# Create your views here.


class UserView(APIView):
    permission_classes = [permissions.AllowAny]
    # permission_classes = [RegistedMoreThanAWeekUser]

    def get(self,request):
        all_users = UserModel.objects.all()

        # return Response(UserSerializer(request.user).data) # user 가 나 일때
        return Response(UserSerializer(all_users, many=True).data, status= status.HTTP_200_OK)
        
        # 역참조 연습할 때 볼 것. _set 주의
        # user = request.user
        # hobbys = user.userprofile.hobby.all()
        # for hobby in hobbys:
        #     hobby_members = hobby.userprofile_set.exclude(user=user).annotate(username=F('user__username')).values_list('username', flat=True)
        #     hobby_members = list(hobby_members)
        #     print(f"hobby : {hobby.name} / hobby members : {hobby_members}" )

    def post(self,request):
        return Response({"message" : "post method!!"})

    def put(self,request):
        return Response({"message" : "put method!!"})

    def delete(self,request):
        return Response({"message" : "delete method!!"})

def user_view(request):
    if request.mothod == 'get':
        pass

class UserAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password = password)
        if user:
            login(request,user)
            return Response({"message" : "login success!!"})
        return Response({"message" : "존재하지 않거나 틀린 계정입니다!!"})

    def delete(self, request):
        logout(request)
        return Response({"message" : "logout success!!"})