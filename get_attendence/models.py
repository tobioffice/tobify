from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=20, unique=True)
    section = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.roll_no}"