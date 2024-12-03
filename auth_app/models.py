from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    username = models.CharField(max_length=255, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def is_otp_expired(self):
        if not self.otp_created_at:
            return True
        from django.utils import timezone
        expiry_time = self.otp_created_at + timezone.timedelta(minutes=5)
        return timezone.now() > expiry_time


class Note(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.CharField(max_length=255, primary_key=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.author.username}"

    class Meta:
        ordering = ['-created_at']
