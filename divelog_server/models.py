from django.contrib.auth.models import User
from django.db import models

class DiveLog(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.IntegerField()
    dive_site_location = models.CharField(max_length=50)
    max_depth = models.IntegerField()
    dive_duration = models.IntegerField()
    dive_buddy = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.dive_site_location} on {self.date}'

