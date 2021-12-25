from rest_framework_simplejwt.tokens import RefreshToken
from .imports import *
from unidecode import unidecode


@swagger_auto_schema(method='POST', request_body=TokenCreateDto, responses={200: TokenViewDto(many=False)})
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    context = {}
    username = unidecode(request.data.get('username'))
    print("1")
    is_mobile_number = re.compile("^09?\d{9}$", re.IGNORECASE)
    user = None
    if request.data.get('code', None):
        print("2")
        verify_token = VerificationCode.objects.filter(code=request.data.get('code'), name=request.data.get('username'))
        if len(verify_token) > 0:
            print("3")
            q = Q(cellphone=request.data.get('username')) | Q(email=request.data.get('username'))
            user = User.objects.get(q)
        if not user:
            print("4")
            try:
                print("5")
                verify = VerificationCode.objects.get(name=request.POST.get('username'))
                verify.trying += 1
                verify.save()
                if verify.trying > 4:
                    print("6")
                    verify.delete()
                    pass
            except:
                pass
    elif request.data.get('password', None):
        print("7")
        if is_mobile_number.match(username):
            print("8")
            username = User.objects.get(cellphone=request.data.get('username')).username
        else:
            print("9")
            username = User.objects.get(email=request.data.get('username')).username
        user = authenticate(username=username, password=request.data.get('password', None))
    if user:
        refresh = RefreshToken.for_user(user)
        context['access'] = str(refresh.access_token)
        context['refresh'] = str(refresh)
        context['msg'] = "ورود با موفقیت انجام شد"
        context.update(UserSerializer(user).data)
        status_code = HTTP_200_OK
    else:

        context['msg'] = 'نام کاربری یا کد ارسال شده اشتباه می باشد'
        status_code = HTTP_400_BAD_REQUEST
    return Response(context, status=status_code)
