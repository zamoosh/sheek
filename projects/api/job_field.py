from .imports import *
from ..models import JobField
from ..serializer import JobFieldSerializer


@swagger_auto_schema(method='GET', responses={200: JobFieldViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_job_field_parent(request):
    context = {}
    job_field = JobField.objects.filter(parent=None)
    serializer = JobFieldSerializer(job_field, many=True)
    context = serializer.data
    status_code = HTTP_200_OK

    return Response(context, status=status_code)


@swagger_auto_schema(method='GET', responses={200: JobFieldViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_job_field(request, id):
    context = {}
    job_field = JobField.objects.filter(parent_id=id)
    serializer = JobFieldSerializer(job_field, many=True)
    context = serializer.data
    status_code = HTTP_200_OK

    return Response(context, status=status_code)


@swagger_auto_schema(method='GET', responses={200: JobFieldViewDto(many=True)})
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_job_field_field(request, id):
    context = {}
    job_field = JobField.objects.filter(parent_id=id)
    serializer = JobFieldSerializer(job_field, many=True)
    context = serializer.data
    status_code = HTTP_200_OK

    return Response(context, status=status_code)
