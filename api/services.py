from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
import logging

logger = logging.getLogger(__name__)


def send_email_reminder(recipient, message):
    """Send an email reminder to the recipient."""
    try:
        send_mail(
            subject='Reminder from Remind-Me-Later',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient],
            fail_silently=False,
        )
        logger.info(f"Email sent to {recipient}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email to {recipient}: {e}")
        return False


def send_sms_reminder(recipient, message):
    """Send an SMS reminder to the recipient."""
    try:
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=settings.TWILIO_PHONE_NUMBER,
            to=recipient
        )
        logger.info(f"SMS sent to {recipient}")
        return True
    except Exception as e:
        logger.error(f"Failed to send SMS to {recipient}: {e}")
        return False


def send_reminder(reminder):
    """Send a reminder via the appropriate method."""
    if reminder.reminder_method == 'email':
        success = send_email_reminder(reminder.recipient, reminder.message)
    elif reminder.reminder_method == 'sms':
        success = send_sms_reminder(reminder.recipient, reminder.message)
    else:
        logger.error(f"Unknown reminder method: {reminder.reminder_method}")
        return False

    if success:
        reminder.is_sent = True
        reminder.save()
        return True
    return False