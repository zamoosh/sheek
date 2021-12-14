from .imports import *
from unidecode import unidecode


@swagger_auto_schema(method='POST', request_body=UserInfoGetDto, responses={200: UserInfoDto(many=False)})
@api_view(['POST'])
@permission_classes((AllowAny,))
def user_info(request):
    if request.method == "POST":
        context = {}
        username = unidecode(request.data.get('username', '').lower())
        is_mobile_number = re.compile("^09?\d{9}$", re.IGNORECASE)
        user = None
        if is_mobile_number.match(username):
            if User.objects.filter(cellphone=username):
                user = User.objects.get(cellphone=username)
        elif '@' in username:
            if User.objects.filter(email=username):
                user = User.objects.get(email=username)
        status_code = HTTP_200_OK
        if user:
            status_code = HTTP_200_OK
            context['new_user'] = False
            if len(user.password) == 0:
                context['has_password'] = False
            else:
                context['has_password'] = True
            context['first_name'] = user.first_name
            context['last_name'] = user.last_name
            context['birthday'] = user.birthday
            context['fullname_length'] = len(user.get_full_name())
        else:
            context['new_user'] = True
            context['has_password'] = False
            context['first_name'] = None
            context['last_name'] = None
            context['birthday'] = None
            context['fullname_length'] = 0

    return Response(context, status=status_code)
