from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

    class Meta:
        unique_together = ('user', 'street', 'city', 'state', 'zip_code')

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"
    

class AssessmentOrder(models.Model):

    STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('assigned', 'Assigned'),
    ('complete', 'Complete'),
    ]

    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='order')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order #{self.id} for {self.address} on {self.created_at.date()}"

