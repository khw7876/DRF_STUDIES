import imp
from unittest import result
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from django.contrib.auth import authenticate, login, logout

# Create your views here.


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        return Response({"message" : "get method!!"})
        
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
        print(f"user : {user}")
        if user:
            login(request,user)
            return Response({"message" : "login success!!"})
        return Response({"message" : "존재하지 않거나 틀린 계정입니다!!"})

    def delete(self, request):
        logout(request)
        return Response({"message" : "logout success!!"})