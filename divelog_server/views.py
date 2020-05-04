from .serializers import DiveLogSerializer
from .models import DiveLog
from rest_framework import generics

class DiveLogList(generics.ListCreateAPIView):
    queryset = DiveLog.objects.all()
    serializer_class = DiveLogSerializer