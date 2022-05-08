from .imports import *

@login_required
def experts(request):
    context = {}
    context['experts_ok'] = UserJobField.objects.filter(status=True, delete=False).order_by('-id')
    context['experts'] = UserJobField.objects.filter(status=False, delete=False).order_by('-id')
    if 'confirm' in request.GET:
        context['getexperts'] = UserJobField.objects.get(id=int(request.GET.get('confirm')))
        context['getexperts'].status = True
        context['getexperts'].save()
        context['confirm'] = True

    if 'reject' in request.GET:
        context['getexperts'] = UserJobField.objects.get(id=int(request.GET.get('reject')))
        context['getexperts'].delete = True
        context['getexperts'].status = False
        context['getexperts'].save()
        context['reject'] = False
    return render(request, 'project/experts.html', context)
