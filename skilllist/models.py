from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    prereq = models.CharField(max_length=200)
    activation = models.CharField(max_length=200)
    recharge = models.CharField(max_length=200)
    castrange = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    version = models.IntegerField()
    

    def __str__(self):
        return self.name