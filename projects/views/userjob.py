from .imports import *

@login_required
def userjobfield(request):
    context = {}
    context['userjobs'] = UserJobField.objects.filter(owner=request.user.id).order_by('-id')
    return render(request, 'project/userjob.html', context)
