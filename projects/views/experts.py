from .imports import *

@login_required
def experts(request):
    context = {}
    context['experts'] = UserJobField.objects.all()
    if 'confirm' in request.GET:
        context['getexperts'] = UserJobField.objects.get(id=int(request.GET.get('confirm')))
        context['getexperts'].status = 1
        context['getexperts'].save()
        context['result'] = True
    if 'reject' in request.GET:
        context['getexperts'] = UserJobField.objects.get(id=int(request.GET.get('reject')))
        context['getexperts'].status = 0
        context['getexperts'].save()
        context['result'] = False
    return render(request, 'project/experts.html', context)