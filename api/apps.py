# Step 6: Update the apps.py file to start the scheduler when the app is ready
# remind_me_later/api/apps.py
from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Import after app is ready to avoid AppRegistryNotReady exception
        from . import scheduler
        scheduler.start_scheduler()
