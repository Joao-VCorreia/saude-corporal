from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('healthhub/', include('HealthHub.urls')),
    path('admin/', admin.site.urls),
]
