from django.db.models import Q

from .imports import *

def reports(request):
    context = {}
    context['all_user'] = User.objects.all()
    context['all_experts'] = User.objects.filter(has_jobField=True)
    context['all_admins'] = User.objects.filter(is_superuser=True)
    context['all_projects'] = Project.objects.all()
    context['done'] = Project.objects.filter(status_jobField_user=2)
    context['progress'] = Project.objects.filter(status_jobField_user=1)
    context['before_confirm'] = Project.objects.filter(status_jobField_user=0)
    context['state'] = State.objects.filter(status=True, parent=None)
    context['city'] = State.objects.filter(~Q(parent=None), status=True)
    return render(request, 'log/reports.html', context)
