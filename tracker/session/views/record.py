from django.core.exceptions import ValidationError
from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class RecordAttendance(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        from session.models import Session, Record
        try:
            session = Session.objects.get(key=data['key'])
        except ValidationError or Session.DoesNotExist:
            return Response({'message': 'Session not found'}, status=404)
        if timezone.now() < session.start_time:
            return Response({'message': 'Session not started yet'}, status=400)
        if timezone.now() > session.end_time:
            return Response({'message': 'Session ended'}, status=400)
        from tracker.models import Log
        if not Log.objects.filter(
            device__user=request.user,
            timestamp__gte=session.start_time,
            timestamp__lte=session.end_time
        ).exists():
            return Response({'message': 'You are not allowed to perform this action'}, status=401)
        if Record.objects.filter(session=session, user=request.user).exists():
            return Response({'message': 'You have already recorded your attendance'}, status=400)
        Record.objects.create(
            session=session,
            user=request.user
        )
        return Response({'message': 'Attendance recorded successfully'}, status=200)


__all__ = [
    'RecordAttendance'
]
