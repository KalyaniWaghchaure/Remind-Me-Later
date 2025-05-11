# Step 3: Create serializers.py
# remind_me_later/api/serializers.py
from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'date', 'time', 'message', 'reminder_method', 'recipient', 'created_at', 'is_sent']
        read_only_fields = ['id', 'created_at', 'is_sent']
