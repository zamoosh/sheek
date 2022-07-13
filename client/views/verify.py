from django.urls import reverse

from .imports import *


def verify(request):
    context = {}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('client:dashboard'))
    if 'user' in request.session:
        context = request.session['user']
        if request.method == 'POST':
            if request.POST.get("verify_code", "") == str(request.session['key']):
                if User.objects.filter(cellphone=context['cellphone']).exists():
                    user = User.objects.get(cellphone=context['cellphone'])
                    if user is not None:
                        if user.is_active:
                            login(request, user)
                            del request.session['user']
                            if len(request.GET.get("next", "/")) == 0:
                                return HttpResponseRedirect("/")
                            return HttpResponseRedirect(request.GET.get("next", "/"))
                        else:
                            context['active'] = False
                    else:
                        print("The username and password were incorrect.")
            else:
                context['error'] = 1
        else:
            if not User.objects.filter(username=context['cellphone']).exists():
                u = User()
                u.cellphone = context['cellphone']
                u.username = context['cellphone']
                u.save()
            u = User.objects.get(username=context['cellphone'])
            try:
                u.sendsms()
                key = u.get_verificationcode()
                request.session['key'] = key
                return render(request, "client/verify.html", context)
            except:
                context['sms'] = False
                return HttpResponseRedirect("/accounts/auth/")
        return render(request, "client/verify.html", context)
    else:
        return HttpResponseRedirect("/accounts/")