from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    fees = models.DecimalField(max_digits=9, decimal_places=3)

