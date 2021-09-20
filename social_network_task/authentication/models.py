from django.db import models
from datetime import datetime, timedelta
from django.conf import settings 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import jwt


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """ Create and return user object. """
        if username is None:
            raise TypeError('No username.')

        if email is None:
            raise TypeError('No email.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """ Create and return superuser object. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    
    @property
    def token(self):
        """ Generates and returns user's JWT token """
        return self._generate_jwt_token()

    def get_full_name(self):
        """ Returns user's username """
        return self.username

    def get_short_name(self):
        """ Returns user's username """
        return self.username

    def _generate_jwt_token(self):
        """ Generates JWT token """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': 1663696078
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.encode().decode('utf-8')