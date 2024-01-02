# myapp/urls.py

from django.urls import path
from .views import read_excel_data

urlpatterns = [
   path('read-excel/<str:file_name>/', read_excel_data, name='read_excel_data'),
]
