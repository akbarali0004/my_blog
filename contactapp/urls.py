from django.urls import path
from .views import sendMessage


urlpatterns = [
    path('', sendMessage, name='send_message')
]
