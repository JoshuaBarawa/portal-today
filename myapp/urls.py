
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('app/v1/', include('app.urls')),
    path('admin/', admin.site.urls),
]
