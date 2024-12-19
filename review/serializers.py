from rest_framework import serializers
from .models import Review

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Review
        fields = '__all__'
