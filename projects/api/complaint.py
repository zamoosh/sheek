from .imports import *
from projects.models import *
from ..serializer import ComplaintSerializer, TextSerializer


@swagger_auto_schema(method='POST', request_body=ComplaintCreateDto, responses={201: ComplaintViewDto(many=False)})
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_complaint(request):
    context = {}
    complaint = Complaint(title=request.data.get('title'))
    complaint.project = Project.objects.get(id=request.data.get('project', 0))
    complaint.type = 1
    complaint.save()
    context['complaint'] = ComplaintSerializer(complaint, many=False).data
    text = Text(owner=request.user, complaint=complaint)
    text.text = request.data.get('text', '')
    text.save()
    context['text'] = TextSerializer(text, many=False).data
    context['msg'] = 'شکایت با موفقیت ثبت شد '
    status_code = HTTP_201_CREATED
    return Response(context, status=status_code)


@swagger_auto_schema(method='GET', responses={201: ComplaintViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_complaint_list(request):
    complaint = Complaint.objects.filter(project__in=Project.objects.filter(owner=request.user))
    serializer = ComplaintSerializer(complaint, many=True).data
    status_code = HTTP_201_CREATED
    return Response(serializer, status=status_code)


@swagger_auto_schema(method='GET', responses={201: ComplaintViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_complaint_one(request, id):
    context = {}
    complaint = Complaint.objects.get(id=id)
    context['complaint'] = ComplaintSerializer(complaint, many=False).data
    context['text'] = TextSerializer(Text.objects.filter(complaint_id=id), many=True).data
    status_code = HTTP_201_CREATED
    return Response(context, status=status_code)


@swagger_auto_schema(method='POST', request_body=TextCreateDto, responses={201: TextViewDto(many=False)})
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_text(request):
    context = {}
    text = Text(owner=request.user)
    text.complaint = Complaint.objects.get(id=request.data.get('complaint', 0))
    text.text = request.data.get('text', 0)
    text.save()
    context['text'] = TextSerializer(text, many=False).data
    context['msg'] = 'پیام شما با موفقیت ثبت شد '
    status_code = HTTP_201_CREATED
    return Response(context, status=status_code)


@swagger_auto_schema(method='GET', responses={201: ComplaintViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_complaint_done(request, id):
    context = {}
    complaint = Complaint.objects.get(id=id)
    complaint.status = True
    complaint.save()
    context['complaint'] = ComplaintSerializer(complaint, many=False).data
    status_code = HTTP_200_OK
    return Response(context, status=status_code)
