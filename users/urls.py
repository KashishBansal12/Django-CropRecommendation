# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.recommendation_history, name='recommendation_history'),
    path('signup/', views.signup, name='signup'), # Add this line
]