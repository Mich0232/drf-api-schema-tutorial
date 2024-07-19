from projects.models import Project, Task
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    extra_field = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ["pk", "name", "project", "assignee", "extra_field"]

    def get_extra_field(self, instance: Task) -> int:
        return id(instance)
