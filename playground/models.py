from __future__ import unicode_literals
from django.db import models
import bcrypt
import datetime

class GameManager(models.Manager):
    def basic_validator(self, postData):
        # todays_date = datetime.datetime.now()
        # date = datetime.datetime.strptime(postData['date'], '%Y-%m-%d')
        errors={}
        if len(postData['state'])>3:
            errors["state"]="State needs to follow the format ex: CA, WA, NV, etc."
        if len(postData['zipcode'])>6:
            errors['zipcode']="The Zip Code needs to be 5 digits."
        # if len(postData['date'])<1:
        #     errors['date'] = "A date MUST be provided"
        # if date <= todays_date:
        #     errors['date'] = "Date needs to be in the future"
        return errors

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
    joiner=models.ManyToManyField("login.User", related_name="join_game")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=GameManager()

