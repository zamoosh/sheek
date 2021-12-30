from projects.models import *
from .imports import *
from datetime import timedelta
import datetime
from ..serializer import ExpertSerializer

manual_parameter = [
    openapi.Parameter('state', openapi.IN_QUERY, description="state id", type=openapi.TYPE_INTEGER,
                      required=True),
    openapi.Parameter('jobField', openapi.IN_QUERY, description="jobfield id ", type=openapi.TYPE_INTEGER,
                      required=True)]


# show user jobfields for choice expert
@swagger_auto_schema(method='GET', manual_parameters=manual_parameter, responses={200: UserJobFieldViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_choice(request):
    context = []
    jobField = request.GET.get('jobField')
    state = State.objects.get(id=request.GET.get('state'))
    q = Q()
    q = q & Q(status=True, jobField=JobField.objects.get(id=jobField))
    experience = UserJobField.objects.values_list('experience', flat=True).filter(q)
    five_delta = datetime.now() - datetime.timedelta(days=1825)
    ten_delta = datetime.now() - datetime.timedelta(days=3650)
    if experience >= five_delta:
        expert_id = UserJobField.objects.values_list('owner', flat=True).filter(q, state=state).distinct()
        expert = User.objects.filter(id__in=expert_id)
    elif ten_delta <= experience < five_delta:
        expert_id = UserJobField.objects.values_list('owner', flat=True).filter(q, state__in=State.objects.filter(
            parent_id=state.parent)).distinct()
        expert = User.objects.filter(id__in=expert_id)
    elif experience < ten_delta:
        expert_id = UserJobField.objects.values_list('owner', flat=True).filter(q).distinct()
        expert = User.objects.filter(id__in=expert_id)

    serializer = UserSerializer(expert, many=True)
    context = serializer.data
    status_code = HTTP_200_OK

    return Response(context, status=status_code)
