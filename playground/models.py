from __future__ import unicode_literals
from django.db import models
import bcrypt
import datetime
from pytz import timezone

class GameManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        todays_date=datetime.datetime.now(timezone("US/Pacific")).strftime("%Y-%m-%d %H:%M:%S")
        todays_date = datetime.datetime.strptime(todays_date,"%Y-%m-%d %H:%M:%S")
        print(todays_date)
        # todays_date= datetime(todays_date.year, todays_date.month, todays_date.day, todays_date.hour, todays_date.minute, todays_date.second)

        if len(postData['sport'])<1:
            errors['sport']="A Sport must be provided"
        if len(postData['sport'])>26:
            errors['sport']="A Sport name is too long"

        if len(postData['location'])<1:
            errors['location']="A Location must be provided"

        if len(postData['zipcode'])<1:
            errors['zipcode']="A Zip Code must be provided"

        if len(postData['city'])<1:
            errors['city']="A City name must be provided"
        if len(postData['city'])>51:
            errors['city']="A City name is too long"

        if len(postData['state'])<1:
            errors["state"]="State needs to follow the format ex: CA, WA, NV, etc."
        if len(postData['state'])>=3:
            errors["state"]="State needs to follow the format ex: CA, WA, NV, etc."

        if len(postData['zipcode'])<1:
            errors['zipcode']="The Zip Code needs to be 5 digits."
        if len(postData['zipcode'])>6:
            errors['zipcode']="The Zip Code needs to be 5 digits."

        if len(postData['date'])<1 or len(postData['time'])<1:
            errors['date'] = "Both a start date and a time MUST be provided"
        else:
            date = datetime.datetime.strptime(postData['date'], '%Y-%m-%d')
            time = datetime.datetime.strptime(postData['time'], '%H:%M')
            date=datetime.datetime(date.year, date.month, date.day, time.hour, time.minute)
            print(date)
            print(todays_date)

            if date < todays_date:
                errors['date'] = "Start date needs to be in the future"
        
        return errors

class Game(models.Model):
    location=models.CharField(max_length=255)
    state=models.CharField(max_length=3)
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

