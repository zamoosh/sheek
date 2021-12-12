from .imports import *
from library.smsir import Smsir
from random import randrange
from unidecode import unidecode

from ..dto import *


@swagger_auto_schema(method='POST', request_body=Verify, responses={200: TokenViewDto(many=False)})
@api_view(['POST'])
@permission_classes((AllowAny,))
def get_verify_code(request):
    context = {}
    username = unidecode(request.data.get('username'))
    is_mobile_number = re.compile("^09?\d{9}$", re.IGNORECASE)

    if is_mobile_number.match(username):
        if User.objects.filter(cellphone=username):

            if VerificationCode.objects.filter(name=username):
                VerificationCode.objects.filter(name=username).delete()

            sms = Smsir()
            code = VerificationCode.objects.create(code=randrange(1000, 9999, 1), name=username).code
            sms.sendwithtemplate({'verificationCode': code}, username, 55907)
            context['msg'] = 'رمز یک بار مصرف برای شما پیامک گردید'
            context['new_user'] = False
            return Response(context, status=HTTP_200_OK)
        else:
            sms = Smsir()
            code = VerificationCode.objects.create(code=randrange(1000, 9999, 1), name=username).code
            sms.sendwithtemplate({'verificationCode': code}, username, 1387)
            context['msg'] = 'رمز یک بار مصرف برای شما پیامک گردید'
            context['new_user'] = True
            return Response(context, status=HTTP_200_OK)
    else:
        if User.objects.filter(email=username):

            if VerificationCode.objects.filter(name=username):
                VerificationCode.objects.filter(name=username).delete()

            code = VerificationCode.objects.create(code=randrange(1000, 9999, 1), name=username).code
            send_mail_func(code, username)
            context['msg'] = 'رمز یک بار مصرف برای شما ایمیل گردید'
            context['new_user'] = False
            return Response(context)
        else:
            code = VerificationCode.objects.create(code=randrange(1000, 9999, 1), name=username).code
            send_mail_func(code, username)
            context['msg'] = 'رمز یک بار مصرف برای شما ایمیل گردید'
            context['new_user'] = True
            return Response(context, status=HTTP_200_OK)
