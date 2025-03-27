# describes the process of going from python to json
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from user.serializers import UserSerializer


class Library_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = ['book_id','book_title', 'book_author','genre', 'book_summary', 'book_content','created_at']

