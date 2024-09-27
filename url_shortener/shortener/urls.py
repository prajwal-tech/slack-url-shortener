from django.urls import path
from .views import shorten_url, redirect_url, slack_shortener  # Add slack_shortener here

urlpatterns = [
    path('', shorten_url, name='shorten_url'),
    path('<str:short_code>/', redirect_url, name='redirect_url'),
    path('slack/', slack_shortener, name='slack_shortener'),  # Add this path
]
