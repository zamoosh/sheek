from .imports import *


def verify(request):
    context = {}
    if 'user' in request.session:
        context = request.session['user']
        if request.method == 'POST':
            if request.POST.get("verify_code", "") == str(request.session['key']):
                pattern = re.compile("^\+989?\d{9}$", re.IGNORECASE)
                if pattern.match(context['cellphone']) is None:
                    context['cellphone'] = "+989" + context['cellphone'][2:]
                if User.objects.filter(cellphone=context['cellphone']).exists():
                    user = User.objects.get(cellphone=context['cellphone'])
                    if user is not None:
                        # the password verified for the user
                        if user.is_active:
                            login(request, user)
                            if len(request.GET.get("next", "/")) == 0:
                                return HttpResponseRedirect("/")
                            return HttpResponseRedirect(request.GET.get("next", "/"))
                    else:
                        # the authentication system was unable to verify the username and password
                        print("The username and password were incorrect.")
                else:
                    user = User.objects.create_user(
                        cellphone=context['cellphone'],
                        username=context['cellphone']
                    )
                    user.save()
                    del request.session['user']
                    context['register'] = 1
                    if context['register']:
                        if user.is_active:
                            login(request, user)
                            return HttpResponseRedirect("/profile/profile")
            else:
                context['error'] = 1
        else:
            import random
            try:
                sms = Smsir()
                key = str(random.randrange(10000, 99999))
                request.session['key'] = key
                sms.sendwithtemplate({'verificationCode': key}, context['cellphone'], 55907)
                return render(request, "client/verify.html", context)
            except:
                context['sms'] = False
                return HttpResponseRedirect("/profile/singing")
        return render(request, "client/verify.html", context)
    else:
        return HttpResponseRedirect("/profile")