from django.urls import path
from .views import ContactsListAPIView

urlpatterns = [
    path('', ContactsListAPIView.as_view())
]