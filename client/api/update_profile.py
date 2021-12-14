from .imports import *


@swagger_auto_schema(method='PUT', request_body=UpdateProfileCreateDto, responses={200: UserViewDto(many=False)})
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_profile(request):
    user = User.objects.filter(id=request.user.id)
    user.update(**request.data)
    user = User.objects.get(id=request.user.id)
    if request.data.get('password', None):
        user.set_password(request.data.get('password'))
        user.save()
    return Response(UserSerializer(user, many=False).data, status=HTTP_200_OK)
