from projects.models import *
from .imports import *
from datetime import timedelta
import datetime

@login_required
def project_request(request):
    context = {}
    current_user = UserJobField.objects.filter(owner=request.user.id)
    five_delta = datetime.date.today() - datetime.timedelta(days=5 * 365)
    ten_delta = datetime.date.today() - datetime.timedelta(days=10 * 365)
    context['projects'] = []
    for cuser in current_user:
        if cuser.expiration > five_delta:
            context['projects'] += Project.objects.filter(user_jobField=None,
                                                         jobField=cuser.jobField).order_by('-created_at')
        elif cuser.expiration > ten_delta:
            context['projects'] += Project.objects.filter(user_jobField=None,
                                                         jobField=cuser.jobField).order_by('-created_at')
        else:
            context['projects'] += Project.objects.filter(user_jobField=None, jobField=cuser.jobField).order_by('-created_at')
        if 'confirm' in request.GET:
            context['getProject'] = Project.objects.get(id=int(request.GET.get('confirm')))
            context['getProject'].user_jobField_id = cuser.id
            context['getProject'].status_jobField_user = True
            context['getProject'].save()
            context['result'] = True
    return render(request, 'project/project-request.html', context)
