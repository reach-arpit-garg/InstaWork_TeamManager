from django.db import models

# Create your models here.
import uuid # Required for unique member instances
from phone_field import PhoneField # Required for phone number of the members
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Member(models.Model):
    """Model representing a specific team member."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for a particular member')
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=254)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')

    ROLE_STATUS = (
        ('r', 'Regular'),
        ('a', 'Admin'),
    )

    role = models.CharField(
        max_length=1,
        choices=ROLE_STATUS,
        blank=True,
        default='r',
        help_text='Role of the member',
    )
    
    def __str__(self):
        """String for representing the Model object."""
        return str(self.id)