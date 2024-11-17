from django.db import models

# Create your models here.
class Team(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    profile_photo = models.ImageField(upload_to='profiles')

    def __str__(self):
        return f"{self.full_name} ----> {self.position}"



class Analytic(models.Model):
    clients = models.IntegerField()
    projects = models.IntegerField()
    HoursOfSupport = models.IntegerField()
    workers = models.IntegerField()

    def __str__(self):
        return "siteAnalytics"