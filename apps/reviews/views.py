from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer

class ProductReview(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer