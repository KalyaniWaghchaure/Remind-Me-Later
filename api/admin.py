# Step 8: Register the model in admin.py
# remind_me_later/api/admin.py
from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'message', 'reminder_method', 'recipient', 'is_sent')
    list_filter = ('date', 'reminder_method', 'is_sent')
    search_fields = ('message', 'recipient')
