from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('superadmin', 'Super Admin'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
    )

    USER_TYPE_STATUS_MAP = {
        'superadmin': 'Superuser',
        'staff': 'Staff',
        'customer': 'Customer',
    }

    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='customer')

    name = models.CharField(max_length=255, default='')
    email = models.EmailField()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # Map the user_type to the corresponding status
        self.is_superuser = self.USER_TYPE_STATUS_MAP.get(self.user_type) == 'Superuser'
        self.is_staff = self.USER_TYPE_STATUS_MAP.get(self.user_type) == 'Staff'

        super().save(*args, **kwargs)