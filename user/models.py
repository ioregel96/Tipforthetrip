from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
import datetime

import uuid

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, **additional_fields):
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **additional_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **additional_fields):
        additional_fields.setdefault("is_staff", True)
        additional_fields.setdefault("is_superuser", True)

        if additional_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")
        if additional_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")

        return self.create_user(email=email, password=password, **additional_fields)


class User(AbstractUser):
    id = models.UUIDField(verbose_name="user id", primary_key=True, default=uuid.uuid4)
    username = None
    email = models.EmailField(verbose_name="email adress", max_length=60, unique=True)
    user_role = models.IntegerField(verbose_name="user role")
    first_name = models.CharField(verbose_name="first name", max_length = 50)
    last_name = models.CharField(verbose_name="last name", max_length = 50)
    is_subscribed = models.BooleanField(verbose_name="is_subscribed",default=False)
    created_at = models.DateTimeField(verbose_name="created_at",auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name="updated_at",auto_now=True, editable=False)

    objects=UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_role", "first_name", "last_name"]

    def __str__(self):
        return str(self.id)


class Contact(models.Model):
    user_id = models.ManyToManyField(User,verbose_name="users(s)", blank=True)
    street_address = models.TextField(max_length=100)
    zip_code = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.street_address}, {self.state} {self.zip_code}"
    