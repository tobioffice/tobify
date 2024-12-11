from django.db import models


class Student(models.Model):
    roll_no = models.TextField(primary_key=True)
    name = models.TextField()
    section = models.TextField()
    branch = models.TextField()
    year = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.roll_no}"

    class Meta:
        managed = False  # Tells Django not to manage this table
        db_table = 'students'  # Name of your existing table
