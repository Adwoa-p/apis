# describes the process of going from python to json
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class Library_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = ['book_id','book_title', 'book_author','genre', 'book_summary', 'book_content','created']


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'password', 'join_date']
        extra_kwargs={'password':{'write_only':True}}


    def create(self,validated_data):
        user=User(
        email=validated_data['email'],
        username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user