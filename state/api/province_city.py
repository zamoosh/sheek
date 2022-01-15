from .imports import *
from ..serializer import ProvinceSerializer


@swagger_auto_schema(method='GET', responses={200: ProvinceViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_province(request):
    context = {}
    province = State.objects.filter(parent=None)
    serializer = ProvinceSerializer(province, many=True)
    context = serializer.data
    status_code = HTTP_200_OK

    return Response(context, status=status_code)


@swagger_auto_schema(method='GET', responses={200: ProvinceViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_city(request, city):
    context = {}
    province = State.objects.filter(parent_id=city)
    serializer = ProvinceSerializer(province, many=True)
    context = serializer.data
    status_code = HTTP_200_OK

    return Response(context, status=status_code)
