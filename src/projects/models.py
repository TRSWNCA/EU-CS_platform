from django.db import models
from django.conf import settings

class Status(models.Model):
    status = models.TextField()
    def __str__(self):        
        return f'{self.status}'

class Project(models.Model):    
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #Database information
    dateCreated = models.DateTimeField('Created date', auto_now=True)
    dateUpdated = models.DateTimeField('Updated date', auto_now=True)
    origin = models.CharField(max_length=100)
    #Basic Project Information
    name = models.CharField(max_length=100)
    aim = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    keywords = models.CharField(max_length=100)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')
    topic = models.CharField(max_length=300)
    #Images and communications
    url = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    imageCredit = models.CharField(max_length=200)
    #Geography
    latitude = models.FloatField()
    longitude = models.FloatField()
    #Personal and Organizational Affiliates
    host = models.CharField(max_length=100)
    #Supplementary information for Citizen Science
    howToParticipate = models.CharField(max_length=300)
    equipment = models.CharField(max_length=200)
    def __str__(self):        
        return f'{self.name}'

class Category(models.Model):
    category = models.TextField()
    def __str__(self):        
        return f'{self.category}'