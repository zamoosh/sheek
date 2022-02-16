from .imports import *
from projects.models import *
from projects.serializer import *


@swagger_auto_schema(method='POST', request_body=ProjectCreateCommentDto,
                     responses={201: ProjectViewCommentDto(many=False)})
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def comment_rate_projects(request, id):
    context = {}
    project = Project.objects.get(id=id, status_jobField_user=1)
    comment = Comment(projects=project)
    comment.text = request.data.get('comment', '')
    comment.save()
    project.rate = request.data.get('rate', 1)
    project.status_jobField_user = 2
    project.save()
    context['comment'] = CommentSerializer(comment, many=False).data
    context['project'] = LowProjectSerializer(project, many=False).data
    context['msg'] = 'پروژه با موفقیت ثبت شد '
    status_code = HTTP_200_OK
    return Response(context, status=status_code)
