from django.urls import path
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from apps.reviews import views

urlpatterns = [
    path('', RedirectView.as_view(url='reviews/', permanent=False)),
    path('reviews/', views.ProductReview.as_view()),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)