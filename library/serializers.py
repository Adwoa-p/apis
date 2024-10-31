# describes the process of going from python to json
from rest_framework import serializers
from .models import Library

class Library_Serializer(serializers.ModelSerializer):
    class Meta: # json data describing the models in our db
        model = Library
        fields = ['book_id', 'book_title', 'book_author']
