from .imports import *
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from ..serializer import PermissionSerializer


@swagger_auto_schema(method='POST', request_body=UserUpdatePermsDto, responses={200: UserInfoDto(many=False)})
@swagger_auto_schema(method='PUT', request_body=UserGroupUpdateDto, responses={200: UserInfoDto(many=False)})
@swagger_auto_schema(method='GET', manual_parameters=[
    openapi.Parameter('id', openapi.IN_QUERY, description="LIST OF USERS", type=openapi.TYPE_ARRAY,
                      items=openapi.Items(type=openapi.TYPE_INTEGER), required=False)])
@api_view(['GET', 'PUT', 'POST'])
@permission_classes((AllowAny,))
def getUserPermission(request):
    if not request.user.is_superuser:
        context = {}
        status_code = ""
        if request.method == "GET":
            q = Q()
            if request.GET.get('id', None):
                q = q & Q(id__in=request.GET.get('id').split(','))
            context['users'] = User.objects.filter(q)
            context['users'] = UserSerializer(context['users'], many=True).data
            status_code = HTTP_200_OK
        if request.method == "PUT":
            context['user'] = User.objects.filter(id=request.data.get('user_id'))
            context['group'] = Group.objects.filter(id=request.data.get('group_id'))
            for us in context['user']:
                for prs in context['group']:
                    us.groups.add(prs)
            del context['group']
            del context['user']
            context['msg'] = "کاربر اضافه شد"
            status_code = HTTP_200_OK
        if request.method == "POST":
            context['user'] = User.objects.filter(id=request.data.get('id'))
            context['permission'] = Permission.objects.filter(id__in=request.data.get('permission'))
            for user in context['user']:
                print(user)
                permission_user = user.get_all_permissions()
                print(permission_user)
                if context['permission'] not in permission_user:
                    for perms in context['permission']:
                        user.user_permissions.add(perms)
                for perms in permission_user:
                    if perms not in context['permission']:
                        user.user_permissions.remove(Permission.objects.get(codename=perms.split('.')[1],
                                                                            content_type__in=ContentType.objects.filter(
                                                                                app_label=perms.split('.')[0])))

            context['permission'] = PermissionSerializer(context['permission'], many=True).data
            context['user'] = UserSerializer(context['user'], many=True).data
            status_code = HTTP_200_OK
        return Response(context, status=status_code)
