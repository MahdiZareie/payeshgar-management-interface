from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/monitoring/', include('monitoring.urls')),
    path('api/v1/inspecting/', include('inspecting.urls')),
    path('api/v1/security/', include('security.urls')),
]
