from .imports import *

@login_required
def userjobfield(request):
    context = {}
    context['userjobs'] = UserJobField.objects.filter(owner=request.user.id, status=True).order_by('-id')
    context['userjobsNotActive'] = UserJobField.objects.filter(owner=request.user.id, status=False).order_by('-id')
    return render(request, 'project/userjob.html', context)
