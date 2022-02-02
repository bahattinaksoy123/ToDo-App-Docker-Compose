from django.contrib.auth.models import User, Group
from django.db.models import fields
from auth2.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = '__all__'