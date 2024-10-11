from django.db import models

class User(models.Model):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=5, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    document_type = models.CharField(max_length=30)
    document_number = models.CharField(max_length=50)
    address = models.TextField(null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    civil_state = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
    


