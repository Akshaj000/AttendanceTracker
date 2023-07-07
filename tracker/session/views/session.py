from datetime import datetime

from django.utils import timezone
from django.utils.timezone import make_aware

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CreateSession(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        if not request.user.is_staff or not request.user.is_superuser:
            return Response({'message': 'You are not allowed to perform this action'}, status=401)
        for key in ['name', 'start_time', 'end_time']:
            if key not in data:
                return Response({'message': f'{key} is required !'}, status=400)
        end_time = datetime(data['end_time']['year'], data['end_time']['month'], data['end_time']['day'], data['end_time']['hour'], data['end_time']['minute'])
        start_time = datetime(data['start_time']['year'], data['start_time']['month'], data['start_time']['day'], data['start_time']['hour'], data['start_time']['minute'])
        from session.models import Session
        session = Session.objects.create(
            name=data['name'],
            start_time=make_aware(start_time),
            end_time=make_aware(end_time),
            instructor=request.user
        )
        return Response({
            'name': session.name,
            'start_time': session.start_time,
            'end_time': session.end_time,
            'instructor': session.instructor.email,
            'key': session.key
        }, status=200)


class GetSessionsView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff or not request.user.is_superuser:
            return Response({'message': 'You are not allowed to perform this action'}, status=401)
        from session.models import Session
        sessions = Session.objects.all()
        data = []
        for session in sessions:
            is_available = timezone.now() >= session.start_time and timezone.now() <= session.end_time
            data.append({
                'name': session.name,
                'start_time': session.start_time,
                'end_time': session.end_time,
                'instructor': session.instructor.email,
                'key': session.key,
                'is_available': is_available
            })
        return Response(data, status=200)


__all__ = [
    'CreateSession',
    'GetSessionsView'
]
