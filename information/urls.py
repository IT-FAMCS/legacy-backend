from django.urls import path
from .views import *


urlpatterns = [
    path('create/', InfoCreate.as_view(), name = "create"),
    path('<short_title>/', InfoUpdateView.as_view({'get': 'retrieve', 'put': 'update'}), name = 'update')
]
