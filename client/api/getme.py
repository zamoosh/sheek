from .imports import *


@swagger_auto_schema(method='GET', responses={200: UserViewDto(many=True)})
@api_view(['GET'])
@permission_classes((AllowAny,))
def api_get_me(request):
    context = {}
    context['user'] = User.objects.filter(id=request.user.id)
    serializer = UserSerializer(instance=context['user'], many=True)
    context = serializer.data
    status_code = HTTP_200_OK

    return Response(context, status=status_code)
