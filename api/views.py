# Step 4: Create views.py
# remind_me_later/api/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Reminder
from .serializers import ReminderSerializer


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"status": "success", "message": "Reminder created successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED,
            headers=headers
        )