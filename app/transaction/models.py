from django.db import models

from app.user.models import User

from django.core.exceptions import ValidationError

class TransactionType(models.Model):

    name = models.CharField(max_length=300)

class Transaction(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    points = models.IntegerField()
    type = models.ForeignKey(TransactionType, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        
        total_points = self.user.transactions.aggregate(total=models.Sum('points'))['total'] or 0
        
        if total_points + self.points < 0:
            raise ValidationError("User's total points cannot go negative.")
        
        super(Transaction, self).save(*args, **kwargs)