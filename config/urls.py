
from django.contrib import admin
from django.urls import path, include
from ai_service import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('modoo/', include('ai_service.urls')),
]
