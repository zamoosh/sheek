from .imports import *
from ..models import Project, UserJobField, JobField
from ..serializer import ProjectSerializer, JobFieldSerializer


@swagger_auto_schema(method='GET', responses={200: ProjectViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_masters_list(request):
    context = {}
    list = Project.objects.filter(owner=request.user).order_by('-update_at')
    serializer = ProjectSerializer(list, many=True)
    context = serializer.data
    status_code = HTTP_200_OK

    return Response(context, status=status_code)


@swagger_auto_schema(method='GET', responses={200: ProjectViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_projects_list(request):
    context = {}
    list = Project.objects.filter(user_jobField__owner=request.user).order_by('-update_at')
    serializer = ProjectSerializer(list, many=True)
    context = serializer.data
    status_code = HTTP_200_OK
    return Response(context, status=status_code)


@swagger_auto_schema(method='GET', responses={200: ProjectViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_one_project(request, id):
    context = {}
    project = Project.objects.get(id=id)
    serializer = ProjectSerializer(project, many=False)
    context = serializer.data
    status_code = HTTP_200_OK
    return Response(context, status=status_code)

