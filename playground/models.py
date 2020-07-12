from __future__ import unicode_literals
from django.db import models
import bcrypt

class Game(models.Model):
    location=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    sport=models.CharField(max_length=25)
    date=models.DateField()
    time=models.TimeField()
    comment=models.TextField()
    captain=models.ForeignKey("login.User", related_name="game", on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

