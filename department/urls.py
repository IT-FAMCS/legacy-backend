from django.urls import path
from .views import *


urlpatterns = [
    path('create/', DepartmentCreate.as_view(), name = "create"),
    path('', DepartmentList.as_view(), name = 'list'),
    path('<short_title>/', DepartmentUpdateView.as_view({'get': 'retrieve', 'put': 'update'}), name = 'update')
]
