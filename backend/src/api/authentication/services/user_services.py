from abc import abstractmethod

from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from api.authentication.models import User


class GetAllUsers:
    @abstractmethod
    def execute(self):
        return User.objects.get_all_users()


class CreateNewUser:
    @abstractmethod
    def execute(self, name: str, password: str , username:str):
        return User.objects.create_user(
            name=name,
            password=password,
            username=username,
        )


class LoginUser:
    @abstractmethod
    def execute(self, username: str, password: str):
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed
        return user
