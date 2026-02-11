from rest_framework import serializers
from .models import TechPost

class TechPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechPost
        fields = ['id', 'title', 'image', 'note', 'created_at']
