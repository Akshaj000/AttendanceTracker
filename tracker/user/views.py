from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class MeView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if not request.user:
            return Response({'message': 'You are not logged in'}, status=401)
        return Response({
            'email': request.user.email,
            'username': request.user.username,
            'name': request.user.name,
            'is_staff': request.user.is_staff,
            'is_superuser': request.user.is_superuser,
        }, status=200)


__all__ = [
    'MeView',
]
