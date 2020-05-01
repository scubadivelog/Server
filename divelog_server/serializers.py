from rest_framework import serializers
from .models import DiveLog

class DiveLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiveLog
        fields = [
            'id', 'creator', 'dive_site_location', 'max_depth',
            'dive_duration', 'dive_buddy', 'created_on'
        ]