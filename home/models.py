from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=122)
    roll = models.IntegerField()
    city = models.CharField(max_length=122)