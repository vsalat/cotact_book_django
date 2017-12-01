from rest_framework import (serializers, viewsets)
from .models import (Contact, Phone)


class PhoneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phone
        fields = ('phone',)


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    phone = PhoneSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = ('first_name', 'second_name', 'patronymic', 'phone')


# ViewSets define the view behavior.
class ContactsViewSetSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
