from projects.models import *
from .imports import *
from datetime import timedelta
import datetime
from ..serializer import ExpertSerializer, UserJobFieldSerializer

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
    expert_list = []
    jobField = request.GET.get('jobField')
    state = State.objects.get(id=request.GET.get('state'))
    q = Q()
    q = q & Q(status=True, jobField=JobField.objects.get(id=jobField))
    five_delta = datetime.date.today() - datetime.timedelta(days=5 * 365)
    ten_delta = datetime.date.today() - datetime.timedelta(days=10 * 365)
    experience_five = UserJobField.objects.values_list('owner', flat=True).filter(q, experience__gte=five_delta,
                                                                                  state=state)
    experience_ten = UserJobField.objects.values_list('owner', flat=True).filter(q, experience__lt=five_delta,
                                                                                 experience__gte=ten_delta,
                                                                                 state__parent=state.parent)
    experience_full = UserJobField.objects.values_list('owner', flat=True).filter(q, experience__lte=ten_delta)
    expert_list += experience_five
    expert_list += experience_ten
    expert_list += experience_full
    users = UserSerializer(User.objects.filter(id__in=expert_list), many=True).data
    return Response(users, status=HTTP_200_OK)


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
