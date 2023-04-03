from abc import abstractmethod
from typing import Set, Any, Dict

import jwt
from django.contrib.auth import authenticate, get_user_model
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import exceptions
from api.authentication.models import User
from api.authentication.utils.token import generate_access_token, generate_refresh_token
from api.core import settings


class GetAllUsers:
    @abstractmethod
    def execute(self):
        return User.objects.get_all_users()


class CreateNewUser:
    @abstractmethod
    def execute(self, name: str, password: str, username: str):
        return User.objects.create_user(
            name=name,
            password=password,
            username=username,
        )


class LoginUser:
    @abstractmethod
    def execute(self, username: str, password: str):
        user = authenticate(username=username, password=password)
        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)
        if not user:
            raise AuthenticationFailed
        return {"access_token": access_token, "refresh_token": refresh_token}
