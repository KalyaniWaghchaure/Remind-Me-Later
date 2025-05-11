# Step 5: Create a scheduler to run the command periodically
# remind_me_later/api/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command
import logging

logger = logging.getLogger(__name__)

def start_scheduler():
    """Start the scheduler to send reminders."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        lambda: call_command('send_reminders'),
        'interval',
        minutes=1,  # Check for reminders every minute
        id='send_reminders',
        replace_existing=True
    )
    scheduler.start()
    logger.info("Scheduler started")
