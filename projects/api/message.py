from .imports import *
from projects.models import *
from projects.serializer import *


@swagger_auto_schema(method='POST', request_body=MessageCreateDto,
                     responses={201: MessageViewDto(many=False)})
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def send_message(request, id):
    context = {}
    message = Message(project=Project.objects.get(id=id), owner=request.user)
    message.created_at = datetime.datetime.now()
    message.text = request.data.get('text', '')
    message.save()
    context['msg'] = 'پیام با موفقیت ثبت شد '
    status_code = HTTP_200_OK
    context['message'] = MessageSerializer(message, many=False).data
    return Response(context, status=status_code)


@swagger_auto_schema(method='GET', responses={200: MessageViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_message(request, id):
    context = {}
    messages = Message.objects.filter(project=Project.objects.get(id=id))
    for message in messages:
        if request.user == message.project.owner:
            message.user_view = True
            message.save()
        elif request.user == message.project.user_jobField.owner:
            message.save()
    serializer = MessageSerializer(messages, many=True)
    context = serializer.data
    status_code = HTTP_200_OK

    return Response(context, status=status_code)
