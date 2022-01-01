from .imports import *
from projects.models import Project, JobField
from projects.serializer import ProjectSerializer, LowProjectSerializer


@swagger_auto_schema(method='POST', request_body=ProjectCreateDto, responses={201: ProjectViewDto(many=False)})
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_projects(request):
    context = {}
    project = Project(title=request.data.get('title'), owner=request.user)
    project.state_id = request.data.get('state', 0)
    project.description = request.data.get('description', '')
    project.jobField = JobField.objects.get(id=request.data.get('jobField', 0))
    if request.data.get('user_jobField') == 0:
        pass
    else:
        project.user_jobField = request.data.get('user_jobField', 0)
    project.save()
    serializer = LowProjectSerializer(project, many=False)
    context.update(serializer.data)
    context['msg'] = 'پروژه با موفقیت ثبت شد '
    status_code = HTTP_200_OK
    return Response(context, status=status_code)
