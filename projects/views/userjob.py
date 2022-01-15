from .imports import *


def userjobfield(request):
    context = {}
    context['userjobs'] = UserJobField.objects.filter(owner=request.user.id)
    return render(request, 'project/userjob.html', context)
