from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, AllowAny
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema

from .serializers import UserSerializer, SignupSerializer, SigninSerializer
from .services.user_services import GetAllUsers, CreateNewUser, LoginUser
from . import docs


@extend_schema(**docs.user_list)
@csrf_exempt
@api_view(("GET",))
@permission_classes((IsAdminUser,))
def list_users(request: Request) -> Response:
    """
    List all users.
    """
    users = GetAllUsers().execute()
    if users:
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_404_NOT_FOUND)


@extend_schema(**docs.signup)
@csrf_exempt
@api_view(("POST",))
@permission_classes((AllowAny,))
def signup(request: Request) -> Response:
    """
    Create a new user.
    """
    serializer = SignupSerializer(data=request.headers)
    if serializer.is_valid(raise_exception=True):
        user = CreateNewUser().execute(**serializer.validated_data)
        if user:
            return Response(status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(**docs.signin)
@csrf_exempt
@api_view(("POST",))
@permission_classes((AllowAny,))
def signin(request: Request) -> Response:
    """
    Login a user.
    """
    print(request.headers)
    serializer = SigninSerializer(data=request.headers)
    if serializer.is_valid():
        user = LoginUser().execute(**serializer.validated_data)
        if user:
            return Response(status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)