from django.db import models

# Create your models here.
class TeamMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    ROLE_CHOICES = (
        ('regular', 'Regular'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='regular')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({'admin' if self.role == 'admin' else 'regular'})"