from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from .serializers import UserSerializer
from .models import User

import jwt
import json
import datetime

class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email'].lower()
        password = request.data['password']
        user = User.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            raise AuthenticationFailed("Email or password are incorrect.")
        
        time_details = json.dumps(
            {
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                "iat":  datetime.datetime.utcnow(),
            },
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder
        )
        
        # TODO: ensure we can still access the expiry time of the token
        response_payload = {
                "user": {
                    'email': user.email,
                    'first_name': user.first_name,
                    'user_id': str(user.id),
                    'last_name': user.last_name,
                    'time_details' : json.loads(time_details)
                }
        }

        response = Response(response_payload)
        token = jwt.encode(response_payload, 'secret', algorithm="HS256")
        response.set_cookie(key="loginJWT", value=token, httponly=True)
        return response

class SignupAndLoginView(APIView):
    # If the email is in the database, just log them in.
    # If the email is not in the database, create a new user and log them in.
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user = User.objects.filter(email=email).first()
        if user is None or not user.check_password(password):
            raise AuthenticationFailed("Email or password are incorrect.")

        time_details = json.dumps(
            {
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                "iat":  datetime.datetime.utcnow(),
            },
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder
        )
        response_payload = {
                "user": {
                    'email': user.email,
                    'first_name': user.first_name,
                    'user_id': str(user.id),
                    'last_name': user.last_name,
                    'time_details' : json.loads(time_details)
                }
        }
        response = Response(response_payload)
        token = jwt.encode(response_payload, 'secret', algorithm="HS256")
        response.set_cookie(key="loginJWT", value=token, httponly=True)
        return response

# Destroy the cookie:
# Note: We are able to do this on the frontend too.
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("loginJWT")
        response.data = {
            "message": "success"
        }
        return response

# Get the current user based on cookie:
class CurrentUserView(APIView):
    def get(self, request):
        token = request.COOKIES.get("loginJWT")
        if not token:
            raise AuthenticationFailed("Unauthenticated")
        try:
            payload = jwt.decode(token, 'secret', algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")
        user = User.objects.get(pk=payload['user']['user_id'])
        serializer = UserSerializer(user)
        return Response(serializer.data)

# Fetch all users:
# Note: Authentication based on if the user is logged in or not. (cookie)
class AllUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'data': {'ok': True,"users": serializer.data}})

class UserView(APIView):
    #Get user by id
    def get(self, request, uuid_str):
        try:
            user = User.objects.filter(pk=uuid_str).first()
            if(user is None):
                return Response({'data': {'ok': False,"message": "User not found"}})
            serializer = UserSerializer(user)
            return Response({'data': {'ok': True,"user": serializer.data}})
        except:
            return Response({'data': {'ok': False,"message": "User not found"}})

    #Update user by id
    def patch(self, request, uuid_str):
        user = User.objects.get(pk=uuid_str)
        if(user is None):
            return Response({'data': {'ok': False,"message": "User not found"}})
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': {'ok': True,"user": serializer.data}})
        return Response({'data': {'ok': False,"message": "User not found"}})

    #Delete user by id
    def delete(self, request, uuid_str):
        try:
            # uid_hex = uuid.UUID(uuid_str).hex
            user = User.objects.filter(pk=uuid_str).first()
            if(user is None):
                return Response({'data': {'ok': False,"message": "User not found"}})
            user.delete()
            return Response({'data': {'ok': True,"message": "User deleted"}})
        except:
            return Response({'data': {'ok': False,"message": "User not found"}})






