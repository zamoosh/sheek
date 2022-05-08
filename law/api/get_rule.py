from library.pagination import Pagination
from .imports import *
from law.models import *
from ..serializer import *


@swagger_auto_schema(method='GET', manual_parameters=[
    openapi.Parameter('title', openapi.IN_QUERY, description="Filter By Title", type=openapi.TYPE_STRING,
                      required=False),
    openapi.Parameter('article', openapi.IN_QUERY, description="Filter By Article", type=openapi.TYPE_STRING,
                      required=False),
    openapi.Parameter('footnote', openapi.IN_QUERY, description="Filter By Footnote", type=openapi.TYPE_STRING,
                      required=False),
    openapi.Parameter('description', openapi.IN_QUERY, description="Filter By Description", type=openapi.TYPE_STRING,
                      required=False)])
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_rule(request, pk):
    if request.method == "GET":
        paginator = Pagination()
        q = Q()
        if 'title' in request.GET:
            q = q & Q(title__contains=request.GET['title'])
        if 'article' in request.GET:
            q = q & Q(article__contains=request.GET['article'])
        if 'footnote' in request.GET:
            q = q & Q(footnote__contains=request.GET['footnote'])
        if 'description' in request.GET:
            q = q & Q(description__contains=request.GET['description'])
        result_page = paginator.paginate_queryset(Rule.objects.filter(q, group=pk), request)
        serializer = RuleSerializers(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
        status_code = HTTP_200_OK
    return Response(context, status=status_code)
