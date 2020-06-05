from django.conf.urls import url, include
from .models import User,UserActivity
from rest_framework import routers, serializers, viewsets

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ['start_time', 'end_time']

class UserSerializer(serializers.ModelSerializer):
    activity_periods = UserActivitySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['ids', 'real_name','tz','activity_periods']