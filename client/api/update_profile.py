from .imports import *


@swagger_auto_schema(method='PUT', request_body=UpdateProfileCreateDto, responses={200: UserViewDto(many=False)})
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_profile(request):
    user = User.objects.get(id=request.user.id)
    if not user.complete_pro:
        user.first_name = request.data.get('first_name', '')
        user.last_name = request.data.get('last_name', '')
        user.birthday = request.data.get('birthday', '')
        user.national_code = request.data.get('national_code', '')
        user.gender = request.data.get('gender', 1)
        user.state_id = request.data.get('state', 0)
        user.complete_pro = True
        user.save()

    else:
        user.first_name = request.data.get('first_name', '')
        user.last_name = request.data.get('last_name', '')
        user.state_id = request.data.get('state', 0)
        user.birthday = request.data.get('birthday', '')
        user.save()

    if request.data.get('password', None):
        user.set_password(request.data.get('password'))
        user.save()
    return Response(UserSerializer(user, many=False).data, status=HTTP_200_OK)
