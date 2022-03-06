from .imports import *


def auth(request):
    context = {}
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    context = {}
    context['error'] = 0
    if request.method == 'POST':
        context['request'] = {}
        context['request']['cellphone'] = request.POST.get('cellphone', '').strip()
        context['request']['existential'] = request.POST.get('existential')
        request.session['user'] = context['request']
        return HttpResponseRedirect('/accounts/verify/')
    return render(request, 'client/auth.html', context)
