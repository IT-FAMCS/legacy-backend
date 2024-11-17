from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from django.db import connection
from .models import user
from .serializer import LoginSerializer
from .serializer import RegistrationSerializer, UserSerializer


class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )

class UpdateUsers(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Получение данных из запроса
            users = request.data.get("users", [])
            if not users:
                return Response({"error": "No 'users' key in the request body"}, status=status.HTTP_400_BAD_REQUEST)

            # Обновление данных в таблице users_user
            with connection.cursor() as cursor:
                for user in users:
                    cursor.execute("""
                        UPDATE users_user
                        SET username = %s, email = %s, first_name = %s, last_name = %s
                        WHERE id = %s
                    """, [
                        user.get("username"),
                        user.get("email"),
                        user.get("first_name"),
                        user.get("last_name"),
                        user.get("id"),
                    ])

            return Response({"status": "success", "message": "Users updated successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UsersAPIView(APIView):
    model = models.user
    serialier_class = UserSerializer
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
import jwt
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

class VerifyTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')

        if not token:
            return Response({'valid': False, 'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return Response({'valid': True, 'user_id': payload['id']}, status=status.HTTP_200_OK)
        except ExpiredSignatureError:
            return Response({'valid': False, 'error': 'Token has expired'}, status=status.HTTP_400_BAD_REQUEST)
        except InvalidTokenError:
            return Response({'valid': False, 'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

