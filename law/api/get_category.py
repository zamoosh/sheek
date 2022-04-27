from .imports import *
from projects.models import *
from ..serializer import *


@swagger_auto_schema(method='GET', responses={201: LawCategoryViewDto(many=False)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_category(request):
    context = {}
    group = Group.objects.all()
    context = LawCategory(group, many=True).data
    status_code = HTTP_200_OK
    return Response(context, status=status_code)
