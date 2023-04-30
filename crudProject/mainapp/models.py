from django.db import models

# Create your models here.
class student_model(models.Model):
    s_roll=models.IntegerField()
    s_name=models.CharField(max_length=100)
    s_marks=models.IntegerField()
