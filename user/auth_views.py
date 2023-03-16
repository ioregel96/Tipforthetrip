# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.serializers.json import DjangoJSONEncoder

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
        email = request.data['email']
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
        jwt_payload = {
                "user": {
                    'email': user.email,
                    'first_name': user.first_name,
                    'id': user.user_id,
                    'last_name': user.last_name,
                    'time_details' : json.loads(time_details)
                }
        }

        response = Response(jwt_payload)
        token = jwt.encode(jwt_payload, 'secret', algorithm="HS256")
        response.set_cookie(key="loginJWT", value=token, httponly=True)
        # response.data["jwt"] = token
        return response
