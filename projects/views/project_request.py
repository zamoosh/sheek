from projects.models import *
from .imports import *
from datetime import timedelta
import datetime

@login_required
def project_request(request):
    context = {}

    jobField = UserJobField.objects.values_list('jobField', flat=True).filter(owner=request.user)
    state = UserState.objects.values_list('state', flat=True).filter(
        userjobfield__in=UserJobField.objects.filter(owner=request.user))
    q = Q()
    q = q & Q(status=True, user_jobField=None, jobField__in=jobField, state__in=state)
    context['projects'] = Project.objects.filter(q)
    if 'confirm' in request.GET:
        context['getProject'] = Project.objects.get(id=int(request.GET.get('confirm')))
        context['getProject'].user_jobField_id = UserJobField.objects.get(owner=request.user, status=True, jobField=context['getProject'].jobField)
        context['getProject'].status_jobField_user = True
        context['getProject'].save()
        context['result'] = True
    return render(request, 'project/project-request.html', context)
