from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password', 'phone_number'] 
