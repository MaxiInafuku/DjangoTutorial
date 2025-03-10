from django.db import models

# This is a simple way to make it, but a better one is to use models.
'''
class Feature:
    id: int
    name: str
    details: str 
'''

#Don't need to define the id field, since models already have one
class Feature(models.Model):
    name = models.CharField(max_length=20)
    details = models.CharField(max_length=300)  

class Secret(models.Model):
    name = models.CharField(max_length=30)
    details = models.CharField(max_length=500)