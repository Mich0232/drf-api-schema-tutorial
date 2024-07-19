from projects.models import Project, Task
from projects.serializers import ProjectSerializer, TaskSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet, mixins


# List-only view
class ProjectsViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


# List, Create, Update, Retrieve, Delete
class TasksViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
