from django.contrib.auth.base_user import BaseUserManager
from django.db import models



class CustomManager(BaseUserManager):

    
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is must")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)


class Gender(models.Model):
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.gender


class Room(models.Model):
    room_no=models.CharField(max_length=10)

    def __str__(self):
        return self.room_no


class Block(models.Model):
    block_name=models.CharField(max_length=10)

    def __str__(self):
        return self.block_name


class Sharing(models.Model):
    sharing=models.CharField(max_length=10)

    def __str__(self):
        return self.sharing
