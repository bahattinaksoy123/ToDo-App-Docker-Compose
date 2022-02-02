from django.contrib.auth.models import User, Group
from django.db.models import fields
from core.models import Todo
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Todo
        fields = ('id','title','text','date','is_completed', 'user_id')