from .imports import *


@swagger_auto_schema(method='PUT', request_body=UserExpertDto, responses={200: UserViewDto(many=False)})
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def set_expert(request):
    user = User.objects.get(id=request.user.id)
    user.has_jobField = True
    if 'national_card' in request.FILES:
        user.national_card = request.FILES['national_card']
    user.save()

    return Response(UserSerializer(user, many=False).data, status=HTTP_200_OK)

