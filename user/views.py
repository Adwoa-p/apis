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
def login(request):
    username=request.data['username']
    password = request.data['password']

    print(f"Attempting to authenticate: username={username}, password={password}")

    user = authenticate(username=username, password=password)

    if user is None:
        print("Authentication failed")
        return Response({"detail":"Invalid Credentials"}, status = status.HTTP_401_UNAUTHORIZED)
    
    print(f"Authenticated user: {user.username}")
    token, created  = Token.objects.get_or_create(user=user)
    return Response({"token": token.key,"message": " User login successful."})


# method to test authtokens to make sure they work for forbidden requests and to see if user is authenticated
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("passed for {}".format(request.user.email)) # the req passed for the email of the user whose token we just provided


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def user(request):
    if request.method == 'GET':
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data})
    
    elif request.method =='PUT':
        user = get_object_or_404(User, username=request.data.get('username'))
        serializer = UserSerializer(user, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user':serializer.data})
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def logout(request):
    logout(request)
    # return redirect('')
    return Response({"message":"User successfully logged out"})