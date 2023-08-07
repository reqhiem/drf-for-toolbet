from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer, ProjectCreateSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    model_class = Project
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ProjectCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        project_zip = serializer.validated_data.pop("project_zip", None)
        if not project_zip:
            print("No project zip file")
            message = "No project zip file"
        else:
            """ with open(f"assets/files/project-{project_zip.name}", "wb") as f:
                f.write(project_zip.read()) """
            message = "Zip file uploaded"
        serializer.save()
        return Response(data={"message": message}, status=status.HTTP_201_CREATED)
