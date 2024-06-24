"""
This module defines the URL patterns for your Django application's API endpoints, providing
a clear guide to which URLs trigger specific views and their purposes.
"""
from django.urls import path
from agentsWorkflow.views import github_webhook


urlpatterns = [
    path('webhook', github_webhook, name='github_webhook'),
]
