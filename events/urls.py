from django.urls import path
from .views import *


urlpatterns = [
    path('create/', EventCreate.as_view(), name = "create"),
    path('', EventList.as_view(), name = 'list'),
    path('<short_title>/', EventUpdateView.as_view({'get': 'retrieve', 'put': 'update'}), name = 'update')
]
