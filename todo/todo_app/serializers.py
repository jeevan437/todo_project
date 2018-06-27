from rest_framework import serializers
from .models import todo_model

class todo_serializer(serializers.ModelSerializer):
    class Meta:
        model = todo_model
        fields = '__all__'