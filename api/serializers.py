from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "description"]


class ProjectCreateSerializer(serializers.ModelSerializer):
    project_zip = serializers.FileField(
        write_only=True
    )

    class Meta:
        model = Project
        fields = ["name", "description", "project_zip"]
