from .imports import *


def verify(request):
    context = {}
    if 'user' in request.session:
        context = request.session['user']
        if request.method == 'POST':
            if request.POST.get("verify_code", "") == str(request.session['key']):
                if User.objects.filter(cellphone=context['cellphone']).exists():
                    user = User.objects.get(cellphone=context['cellphone'])
                    if user is not None:
                        if user.is_active:
                            login(request, user)
                            if len(request.GET.get("next", "/")) == 0:
                                return HttpResponseRedirect("/")
                            return HttpResponseRedirect(request.GET.get("next", "/"))
                    else:
                        print("The username and password were incorrect.")
                else:
                    user = User.objects.create_user(
                        cellphone=context['cellphone'],
                        username=context['cellphone']
                    )
                    if context['expertRegister']:
                        user.has_jobField = True
                    user.save()
                    del request.session['user']
                    context['register'] = 1
                    if context['register']:
                        if user.is_active:
                            login(request, user)
                            return HttpResponseRedirect("/accounts/profile/")
            else:
                context['error'] = 1
        else:
            import random
            try:
                sms = Smsir()
                # key = str(random.randrange(10000, 99999))
                key = 1234
                request.session['key'] = key
                sms.sendwithtemplate({'verificationCode': key}, context['cellphone'], 55907)
                return render(request, "client/verify.html", context)
            except:
                context['sms'] = False
                return HttpResponseRedirect("/accounts/auth/")
        return render(request, "client/verify.html", context)
    else:
        return HttpResponseRedirect("/accounts/")