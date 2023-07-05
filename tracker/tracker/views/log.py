from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tracker.models import Device, Log


class DeviceLogCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        if 'mac_address' not in data:
            return Response({'message': 'MAC address is required !'}, status=400)
        # Detect or create the device based on the provided MAC address
        try:
            device = Device.objects.get(mac_address__iexact=data['mac_address'])
        except Device.DoesNotExist:
            return Response({'message': 'Device not Registered'}, status=401)

        log = Log(
            device=device,
            meta={
                'mac_address': data['mac_address'],
                **data['meta']
            }
        )
        log.save()

        return Response({'message': 'Device logged successfully'}, status=201)


__all__ = [
    'DeviceLogCreateView'
]
