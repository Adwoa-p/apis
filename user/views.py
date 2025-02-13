from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate
User = get_user_model()
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication # To authenticate sessions with a token
from rest_framework.permissions import IsAuthenticated # to declare that an api only works if user is authenticated
from django.shortcuts import redirect 
from django.contrib.auth.hashers import make_password
import re
# from knox.models import AuthToken


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data= request.data)
    if serializer.is_valid():
        user = User(username=serializer.validated_data['username'],email=serializer.validated_data.get('email'),
                phone_number=serializer.validated_data['phone_number'])
        user.set_password(serializer.validated_data['password']) # password is unique so the hashed version of it is stored
        user.save()
        token = Token.objects.create(user=user) # token for user because they just signed up
        return Response({"message": "User registration successful."})
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signin(request):
    user = get_object_or_404(User, username=request.data['username'])

    # user.password = make_password(user.password)  # hashes the existing password
    # user.save()

    if user is None:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if not user.check_password(request.data['password']):
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
    token, _ = Token.objects.get_or_create(user=user)
    # serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "message": "User login successful."})


# method to test authtokens to make sure they work for forbidden requests and to see if user is authenticated
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    id = request.user.user_id
    return Response("passed for {}".format(id)) # the req passed for the email of the user whose token we just provided


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def user(request):
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        # token, created  = Token.objects.get_or_create(user=user)
        return Response({'user': serializer.data})
    
    elif request.method =='PUT':
        user = get_object_or_404(User, username=request.data.get('username'))
        serializer = UserSerializer(user, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user':serializer.data})
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout(request):
    return Response({"message":"User successfully logged out"})