from rest_framework.viewsets import ModelViewSet
from .models import TaskM
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    queryset = TaskM.objects.all()
    serializer_class = TaskSerializer
