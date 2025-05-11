# Create the management command
# remind_me_later/api/management/commands/send_reminders.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import Reminder
from api.services import send_reminder
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Send pending reminders'

    def handle(self, *args, **options):
        now = timezone.now()
        current_date = now.date()
        current_time = now.time()

        # Get all unsent reminders that are due
        pending_reminders = Reminder.objects.filter(
            is_sent=False,
            date__lte=current_date,
        )

        # Further filter by time for today's reminders
        today_reminders = pending_reminders.filter(date=current_date)
        due_today = [r for r in today_reminders if r.time <= current_time]

        # Get past reminders (previous days)
        past_reminders = pending_reminders.filter(date__lt=current_date)

        # Combine all due reminders
        due_reminders = list(past_reminders) + due_today

        self.stdout.write(f"Found {len(due_reminders)} reminders to send")

        # Send each reminder
        for reminder in due_reminders:
            self.stdout.write(f"Sending reminder to {reminder.recipient}...")
            success = send_reminder(reminder)
            if success:
                self.stdout.write(self.style.SUCCESS(f"Successfully sent reminder to {reminder.recipient}"))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to send reminder to {reminder.recipient}"))

        self.stdout.write(self.style.SUCCESS(f"Processed {len(due_reminders)} reminders"))
