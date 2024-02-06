from django.db import models

# Create your models here.


class Place(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    img=models.ImageField(upload_to="app2/image",null=True,blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    img = models.ImageField(upload_to="app2/image/teams", null=True, blank=True)

    def __str__(self):
        return self.name
