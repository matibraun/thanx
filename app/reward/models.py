from django.db import models
from app.user.models import User

class Reward(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    points_required = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Redemption(models.Model):
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='rewards')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
