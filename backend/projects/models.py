from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    class Department(models.IntegerChoices):
        MAIN = 1, "Main office"
        SECONDARY = 2, "Secondary department"

    name = models.CharField(max_length=255)
    department = models.IntegerField(
        choices=Department.choices, default=Department.MAIN
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, related_name="tasks", on_delete=models.CASCADE)
    assignee = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="tasks"
    )

    def __str__(self):
        return self.name
