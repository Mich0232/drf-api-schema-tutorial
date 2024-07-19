from drf_spectacular.utils import extend_schema, inline_serializer
from projects.models import Project, Task
from projects.serializers import (
    ProjectSerializer,
    TaskNotificationInputSerializer,
    TaskSerializer,
)
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet, mixins


# List-only view
class ProjectsViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


# List, Create, Update, Retrieve, Delete
class TasksViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @extend_schema(
        request=TaskNotificationInputSerializer,
        responses=inline_serializer(
            name="TaskNotificationResponseSerializer",
            fields={"customField": serializers.CharField()},
        ),
    )
    @action(detail=False, methods=["POST"])
    def notify(self, request, *args, **kwargs):
        input_serializer = TaskNotificationInputSerializer(data=request.data.copy())
        input_serializer.is_valid(raise_exception=True)
        input_serializer.save()

        return Response(data={"customField": "success"}, status=status.HTTP_200_OK)


# class AssigneeAPIView(views.APIView):
#     @extend_schema(
#         responses=inline_serializer(
#             name="AssigneeResponseSerializer",
#             fields={
#                 ...
#             },
#         )
#     )
#     def get(self, request, *args, **kwargs):
#         return Response(data={...})
