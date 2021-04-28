from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, serializers
from contacts.serializers import ContactsSerializers
from .models import Contacts


class ContactsListAPIView(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactsSerializers
    queryset = Contacts.objects.filter()

    def get_queryset(self):
        return Contacts.objects.filter(self.request.user)

    def perform_create(self, serializer):
        serializer.save(self.request.user)
