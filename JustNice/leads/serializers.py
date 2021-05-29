from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Lead

# ModelSerializer is like a ModelForm
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')

# Trying to do it for the User model
class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')