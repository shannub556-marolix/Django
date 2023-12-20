
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serilizers import Userserilizer,Detailsserilizer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import authentication_classes,permission_classes,api_view
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated



@api_view(["POST"])
def signup(request):
    if request.method=="POST":
        serilizer1=Detailsserilizer(data=request.data)
        if serilizer1.is_valid():
            serilizer1.save()
        serilizer = Userserilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
        user = User.objects.get(username=request.data['username'])
        token = Token.objects.get(user=user)
        serilizer = Userserilizer(user)
        data = {
            "Note": "User Registration was Sucessful ",
            "details": serilizer.data,
            "token": token.key
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST','GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def login(request):
    if request.method=='POST':
        x=authenticate(username=request.data['username'],password=request.data['password'])
        if x is not None:
            user=User.objects.get(username=request.data['username'])
            serilizer=Userserilizer(user)
            token,new=Token.objects.get_or_create(user=user)
            data={
                "Note" : "Token Succesfully Authinticated and login was sucessfull with given creditentails ",
                'Details': serilizer.data,
                'token' : token.key
            }
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response('Bad Request',status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response({"Note" : "Authorization was Succesful and token deleted ",
        "message": "logout was successful"})