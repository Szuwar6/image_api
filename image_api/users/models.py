from django.contrib.auth.models import User
from django.db import models


class Plan(models.TextChoices):
    BASIC = 'Basic', 'Basic',
    PREMIUM = 'Premium', 'Premium',
    ENTERPRISE = 'Enterprise', 'Enterprise'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    plan = models.CharField(choices=Plan.choices, max_length=10)

    def __str__(self):
        return f"{self.user}"

