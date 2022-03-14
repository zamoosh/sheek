from state.dto import ProvinceViewDto
from state.serializer import ProvinceSerializer
from .imports import *
from ..models import UserJobField, JobField, UserState
from ..serializer import UserJobfieldSerializer, UserStateSerializer


@swagger_auto_schema(method='POST', request_body=UserJobFieldCreateDto,
                     responses={200: UserJobFielddViewDto(many=False)})
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def set_user_jobfied(request):
    for i in request.data.get('jobField'):
        user_jobfield = UserJobField(owner=request.user)
        user_jobfield.jobField = JobField.objects.get(id=i)
        user_jobfield.expiration = request.data.get('expiration', '')
        user_jobfield.issue = request.data.get('issue', '')
        user_jobfield.description = request.data.get('description', '')
        user_jobfield.inquiry_link = request.data.get('inquiry_link', '')
        if 'document_image' in request.FILES:
            user_jobfield.document_image = request.FILES['document_image']
        user_jobfield.save()

    serializer = UserJobfieldSerializer(user_jobfield, many=False).data
    return Response(serializer, status=HTTP_201_CREATED)


@swagger_auto_schema(method='POST', request_body=UserStateCreateDto,
                     responses={200: UserStateViewDto(many=False)})
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def set_state_expert(request, jobfield):
    context = {}
    q = Q()
    q = q & Q(owner=request.user, jobField_id=jobfield, status=True)
    five_delta = datetime.date.today() - datetime.timedelta(days=5 * 365)
    ten_delta = datetime.date.today() - datetime.timedelta(days=10 * 365)
    if UserJobField.objects.filter(q, issue__gte=five_delta):
        user_state = UserState(state=request.user.state)
        user_state.userjobfield = UserJobField.objects.get(q)
        user_state.save()
        context['msg'] = 'کاربر به شهر خود اضافه شد'

    elif UserJobField.objects.filter(q, issue__lt=five_delta, issue__gte=ten_delta):
        for i in request.data.get('state_list'):
            user_state = UserState(userjobfield=UserJobField.objects.get(q))
            user_state.state = State.objects.get(id=i)
            user_state.save()
            context['msg'] = 'کاربر اضافه شد'

    elif UserJobField.objects.filter(q, issue__lte=ten_delta):
        for i in request.data.get('state_list'):
            user_state = UserState(userjobfield=UserJobField.objects.get(q))
            user_state.state = State.objects.get(id=i)
            user_state.save()
            context['msg'] = 'کاربر اضافه شد'

    return Response(context, status=HTTP_201_CREATED)


@swagger_auto_schema(method='GET', responses={200: ProvinceViewDto(many=False)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_state(request, jobfield):
    context = {}
    q = Q()
    q = q & Q(owner=request.user, jobField_id=jobfield, status=True)
    five_delta = datetime.date.today() - datetime.timedelta(days=5 * 365)
    ten_delta = datetime.date.today() - datetime.timedelta(days=10 * 365)
    state = []
    if UserJobField.objects.filter(q, issue__gte=five_delta):
        context['msg'] = 'این کاربر فقط در شهر خود میتواند کار کند'
    elif UserJobField.objects.filter(q, issue__lt=five_delta, issue__gte=ten_delta):
        state = State.objects.filter(parent=request.user.state.parent)
    elif UserJobField.objects.filter(q, issue__lte=ten_delta):
        state = State.objects.all()
        context['msg'] = 'این کاربر دسترسی کامل دارد'

    serializer = ProvinceSerializer(state, many=True).data
    return Response(serializer, status=HTTP_200_OK)
