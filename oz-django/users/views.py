from django.shortcuts import render
from django.contrib.auth.password_validation import validate_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import MyInfoUserSerializer


# Create your views here.
class Users(APIView):
    def post(self, request):
        password = request.data.get('password')
        serializer = MyInfoUserSerializer(data=request.data)

        try:
            validate_password(password)
        except:
            raise ParseError('Invalid password')
        
        if serializer.is_valid():
            user = serializer.save() # 새로운 유저 생성
            user.set_password(password) # 비밀번호 해쉬화
            user.save()

            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            raise ParseError(serializer.errors)

class MyInfo(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user

        serializer = MyInfoUserSerializer(user)

        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)

            return Response(serializer.data)
        else:
            raise ParseError(serializer.errors)

from django.contrib.auth import authenticate, login, logout
from rest_framework import status

class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            raise ParseError()
        
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

class Logout(APIView):
    def post(self, request):
        permission_classes = [IsAuthenticated]
        
        logout(request)

        return Response(status=status.HTTP_200_OK)