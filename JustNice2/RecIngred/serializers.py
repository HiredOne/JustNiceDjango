from rest_framework import serializers
from .models import *

# ModelSerializer is like a ModelForm

class RecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class IngredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class ReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requires
        fields = '__all__'