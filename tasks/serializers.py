from rest_framework import serializers
from .models import TaskM

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskM
        fields = '__all__'
