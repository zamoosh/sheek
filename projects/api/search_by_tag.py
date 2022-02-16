from .imports import *
from ..models import *
from ..serializer import *


@swagger_auto_schema(method='GET', manual_parameters=[
    openapi.Parameter('text', openapi.IN_QUERY, description="search by tag", type=openapi.TYPE_STRING,
                      required=True)])
@api_view(['GET'])
@permission_classes((AllowAny,))
def search(request):
    context = {}
    q = Q()
    q = q & Q(title__contains=request.GET.get('text'))
    result = Tag.objects.filter(q)
    serializer = TagSerializer(result, many=True)
    context = serializer.data
    status_code = HTTP_200_OK
    return Response(context, status=status_code)


@swagger_auto_schema(method='GET', responses={200: JobFieldViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_jobfield_bytag(request, id):
    context = {}
    serializer = JobFieldTagSerializer(Tag.objects.get(id=id).jobfield.all(), many=True)
    context = serializer.data
    status_code = HTTP_200_OK
    return Response(context, status=status_code)


