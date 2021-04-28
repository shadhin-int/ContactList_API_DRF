from rest_framework.serializers import ModelSerializer
from .models import Contacts


class ContactsSerializers(ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'
