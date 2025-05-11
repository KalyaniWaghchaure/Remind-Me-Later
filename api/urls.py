# Step 5: Create urls.py for the API app
# remind_me_later/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReminderViewSet

router = DefaultRouter()
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
