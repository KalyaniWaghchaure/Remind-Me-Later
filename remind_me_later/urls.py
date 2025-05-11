# Step 6: Update the main urls.py
# remind_me_later/remind_me_later/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', RedirectView.as_view(url='api/reminders/', permanent=False)),
]