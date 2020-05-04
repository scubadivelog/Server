from django.urls import path
from .views import DiveLogList

urlpatterns = [
    path('divelog/', DiveLogList.as_view(), name='dive_log'),
]