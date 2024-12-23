from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication # To authenticate sessions with a token
from rest_framework.permissions import IsAuthenticated # to declare that an api only works if user is authenticated
# from knox.models import AuthToken


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password']) # password is unique so the hashed version of it is stored
        user.save()
        token = Token.objects.create(user=user) # token for user because they just signed up
        return Response({"message": "User registration successful."})
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail":"Not found."}, status = status.HTTP_404_NOT_FOUND)
    token, created  = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key,"message": " User login successful."})


# method to test authtokens to make sure they work for forbidden requests and to see if user is authenticated
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.email)) # the req passed for the email of the user whose token we just provided


