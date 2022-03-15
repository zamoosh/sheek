from projects.dto import JobFieldViewDto
from projects.models import *
from projects.serializer import ProjectSerializer, JobFieldSerializer
from .imports import *
from datetime import timedelta
import datetime
from ..serializer import ExpertSerializer, UserJobFieldSerializer, UserJobFieldFieldSerializer

manual_parameter = [
    openapi.Parameter('state', openapi.IN_QUERY, description="state id", type=openapi.TYPE_INTEGER,
                      required=True),
    openapi.Parameter('jobField', openapi.IN_QUERY, description="jobfield id ", type=openapi.TYPE_INTEGER,
                      required=True)]


# show user jobfields for choice expert
@swagger_auto_schema(method='GET', manual_parameters=manual_parameter, responses={200: UserJobFieldViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_user(request):
    q = Q()
    jobField = request.GET.get('jobField')
    q = q & Q(status=True, jobField_id=jobField)

    user_state = UserState.objects.values_list('userjobfield', flat=True).filter(state_id=request.GET.get('state'),
                                                                                 userjobfield__in=UserJobField.objects.filter(
                                                                                     q))
    users = UserJobField.objects.values_list('owner', flat=True).filter(id__in=user_state)
    user = UserSerializer(User.objects.filter(id__in=users), many=True).data
    return Response(user, status=HTTP_200_OK)


@swagger_auto_schema(method='GET', manual_parameters=manual_parameter, responses={200: UserJobFieldViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_expert(request):
    expert_list = []
    context = {}
    jobField = request.GET.get('jobField')
    state = State.objects.get(id=request.GET.get('state'))
    q = Q()
    q = q & Q(status=True, jobField=JobField.objects.get(id=jobField))
    five_delta = datetime.date.today() - datetime.timedelta(days=5 * 365)
    ten_delta = datetime.date.today() - datetime.timedelta(days=10 * 365)
    experience_five = UserJobField.objects.filter(q, experience__gte=five_delta,
                                                  state=state)
    experience_ten = UserJobField.objects.filter(q, experience__lt=five_delta,
                                                 experience__gte=ten_delta,
                                                 state__parent=state.parent)
    experience_full = UserJobField.objects.filter(q, experience__lte=ten_delta)
    expert_list += experience_five
    expert_list += experience_ten
    expert_list += experience_full
    serializer = ExpertSerializer(expert_list, many=True)
    context = serializer.data

    return Response(context, status=HTTP_200_OK)


@swagger_auto_schema(method='GET', manual_parameters=[], responses={200: UserJobFieldViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_expert_one(request, id):
    context = {}
    expert = UserJobField.objects.get(id=id)
    serializer = ExpertSerializer(expert, many=False)
    context = serializer.data
    status_code = HTTP_200_OK
    return Response(context, status=status_code)


@swagger_auto_schema(method='GET', manual_parameters=[], responses={200: ProjectDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_project_for_expert(request):
    context = {}
    jobField = UserJobField.objects.values_list('jobField', flat=True).filter(owner=request.user, status=True)
    state = UserState.objects.values_list('state', flat=True).filter(
        userjobfield__in=UserJobField.objects.filter(owner=request.user))
    q = Q()
    q = q & Q(status=True, user_jobField=None, jobField_id__in=jobField, state_id__in=state)
    project = Project.objects.filter(q)
    serializer = ProjectSerializer(project, many=True).data
    status_code = HTTP_200_OK
    return Response(serializer, status=status_code)


@swagger_auto_schema(method='PUT', request_body=ConfirmDto,
                     responses={200: ProjectDto(many=False)})
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def confirm_project(request, id):
    context = {}
    project = Project.objects.get(id=id)
    print(UserJobField.objects.get(owner=request.user, status=True, jobField=project.jobField))
    project.user_jobField = UserJobField.objects.get(owner=request.user, status=True, jobField=project.jobField)

    project.status_jobField_user = 1
    project.save()
    context['msg'] = 'پروژه اضافه شد'
    return Response(context, status=HTTP_200_OK)


@swagger_auto_schema(method='GET', manual_parameters=[], responses={200: JobFieldViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_jobfield_for_expert(request):
    context = {}
    serializers = UserJobFieldFieldSerializer(UserJobField.objects.filter(owner=request.user), many=True).data
    status_code = HTTP_200_OK
    return Response(serializers, status=status_code)
