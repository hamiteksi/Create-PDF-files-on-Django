from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    donor_name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)