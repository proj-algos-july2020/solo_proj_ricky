from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData, sign_in):
        errors = {}
        if sign_in == 'registration':
            if len(postData['first_name'])<2:
                errors['first_name'] = "First name needs to be longer than 2 characters"
            if len(postData['last_name'])<2:
                errors['last_name'] = "Last name needs to be longer than 2 characters"
            if len(postData['password'])<8:
                errors['password'] = "Password needs to be longer than 8 characters"
            if postData['confirm_password'] != postData['password']:
                errors['confirm_password'] = "Passwords do NOT match"

            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']): # test whether a field matches the pattern
                errors['email'] = ("Invalid email address!")

        elif sign_in == 'login':
            user = User.objects.filter(email=postData['email'])
            if not user:
                errors['user_login'] = 'Incorrect email'
            else:
                if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                    errors['user_password'] = 'Incorrect Password'

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# Create your models here.
