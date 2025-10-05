from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Notification
from .serializer import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        """
        Permite filtrar las notificaciones por user_id si se pasa como parámetro.
        Ejemplo: GET /api/notifications/?user_id=5
        """
        user_id = self.request.query_params.get("user_id")
        if user_id:
            return Notification.objects.filter(user_id=user_id)
        return Notification.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Crea una nueva notificación.
        Espera un JSON con los campos: user_id, title, message, type.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)