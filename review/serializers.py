from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Review
        fields = ['review_id', 'user_id', 'book_id', 'review_text', 'visibility', 'date_posted']
