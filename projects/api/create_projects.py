from .imports import *
from projects.models import Project
from projects.serializer import ProjectSerializer


@swagger_auto_schema(method='POST', request_body=ProjectCreateDto, responses={201: ProjectViewDto(many=False)})
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_projects(request):
    context = {}
    project = Project.objects.get_or_create(title=request.data.get('title'))
    project.owner = User.objects.get(id=int(request.data.get('owner', 0)))
    project.state = request.data.get('state', 0)
    project.description = request.data.get('description', '')
    if request.data.get('status_jobField_user', None):
        project.status_jobField_user = request.data.get('status_jobField_user', 0)
    project.save()
    serializer = ProjectSerializer(project, many=False)
    context.update(serializer.data)
    context['msg'] = 'پروژه با موفقیت ثبت شد '
    status_code = HTTP_200_OK
    return Response(context, status=status_code)
