# describes the process of going from python to json
from rest_framework import serializers
from .models import *


class Library_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = Library
        fields = ['book_id','book_title', 'book_author', 'book_summary','created']
