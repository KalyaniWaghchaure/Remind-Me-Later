# Step 2: Create models.py
# remind_me_later/api/models.py
from django.db import models


class Reminder(models.Model):
    REMINDER_METHODS = (
        ('sms', 'SMS'),
        ('email', 'Email'),
    )

    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_method = models.CharField(max_length=10, choices=REMINDER_METHODS)
    recipient = models.CharField(max_length=100)  # Phone number or email address
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder on {self.date} at {self.time}: {self.message[:20]}..."
