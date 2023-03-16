from rest_framework import serializers
from .models import User, Contact

class UserSerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField('get_contact_info')
    class Meta:
        model = User
        
        fields = ["id", "email", "password", "first_name", "last_name", "user_role","is_subscribed", "contacts", "created_at","updated_at"]
        
        extra_kwargs = {
            'password': {'write_only': True},
            'user_role': {'write_only': True},
        }

    def create(self, validated_data):
        password=validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        if instance.user_role == int(0):
            instance.is_superuser = True
            instance.is_staff = True
        if instance.user_role == int(1):
            instance.is_staff = True
        instance.save()
        return instance
        
    def get_contact_info(self, obj):
        contact_info = Contact.objects.filter(user_id=obj.id)
        serializer = ContactSerializer(contact_info, many=True)
        return serializer.data



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["user_id", "street_address", "zip_code", "state", "phone_number"]


