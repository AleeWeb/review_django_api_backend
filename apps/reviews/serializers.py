from rest_framework import serializers
from .models import Review, LANGUAGE_CHOICES, STYLE_CHOICES


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('review_title', 'username', 'review_date', 'product', 'image_url', 'user_review' )