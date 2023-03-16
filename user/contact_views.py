from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Contact, User
from .serializers import ContactSerializer

# TODO:  Contact Views for CUD operations must be changed to find a user object and the contacts can be found that way

# class CreateContactView(APIView):
    

class ContactCRUDManager(APIView):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        contact = Contact.objects.get(user=user)
        if(contact is None):
            return Response({'data': {'ok': False, "message": "Contact not found"}})
        
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def post(self, request, user_id):
        user = User.objects.get(pk=user_id)
        data = request.data
        data["user_id"] = [user.id]
        print(data)
        serializer = ContactSerializer(data=data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, user_id):
        user = User.objects.get(pk=user_id)
        contact = Contact.objects.get(user=user)
        if(Contact is None):
            return Response({'data': {'ok': False,"message": "Contact not found"}})

        serializer = ContactSerializer(instance=contact, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'data': {'ok': True, "contact": serializer.data}})

    def delete(self, request, user_id):
        user = User.objects.get(pk=user_id)
        contact = Contact.objects.get(user=user)
        if(contact is None):
            return Response({'data': {'ok': False,"message": "Contact not found"}})
        contact.delete()
        return Response({'data': {'ok': True,"message": "Contact deleted"}})