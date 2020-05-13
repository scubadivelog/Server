from .serializers import DiveLogSerializer
from .models import DiveLog
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly

class DiveLogList(generics.ListCreateAPIView):
    queryset = DiveLog.objects.all()
    serializer_class = DiveLogSerializer
    permission_classes = (IsAuthorOrReadOnly) 