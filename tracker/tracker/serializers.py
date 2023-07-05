from rest_framework import serializers
from tracker.models import Device, Log


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['mac_address', 'name', 'type']


__all__ = [
    'DeviceSerializer',
]
