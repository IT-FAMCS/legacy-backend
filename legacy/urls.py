from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/departments/', include('department.urls')),
    path('api/events/', include('events.urls')),
    path('api/info/', include('information.urls')),
    path('api/users/', include('users.urls')),
    path('', include("frontend.urls"))
]
