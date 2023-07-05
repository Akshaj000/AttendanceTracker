from django.db import models
from user.models import User


class Device(models.Model):
    DEVICE_TYPES = [
        ('PHONE', 'Phone'),
        ('LAPTOP', 'Laptop'),
        ('TABLET', 'Tablet')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mac_address = models.CharField(max_length=17)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=DEVICE_TYPES)

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

    def __str__(self):
        return f"{self.user.username} - {self.name} - {self.type}"


__all__ = [
    'Device',
]
