from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serilizers import Userserilizer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate



@api_view(["POST"])
def signup(request):
    if request.method=="POST":
        serilizer = Userserilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
        user = User.objects.get(username=request.data['username'])
        token = Token.objects.get(user=user)
        serilizer = Userserilizer(user)
        data = {
            "details": serilizer.data,
            "token": token.key
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login(request):
    if request.method=='POST':
        x=authenticate(username=request.data['username'],password=request.data['password'])
        if x is not None:
            user=User.objects.get(username=request.data['username'])
            serilizer=Userserilizer(user)
            token=Token.objects.get(user=user)
            data={
                'Details': serilizer.data,
                'token' : token.key
            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_202_ACCEPTED)


def logout(request):
    pass
