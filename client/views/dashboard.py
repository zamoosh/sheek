from django.db.models import Q
from .imports import *

@login_required
def dashboard(request):
    context = {}
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/accounts/auth/")
    jobField = UserJobField.objects.values_list('jobField', flat=True).filter(owner=request.user)
    state = UserState.objects.values_list('state', flat=True).filter(
        userjobfield__in=UserJobField.objects.filter(owner=request.user))
    context['user_jobs'] = UserJobField.objects.filter(owner=request.user, status=True)
    context['projects_progress'] = Project.objects.filter(user_jobField__owner=request.user.id, status=True, status_jobField_user=1).order_by('-id')[:4]
    context['new_projects'] = Project.objects.filter(status=True, user_jobField=None, jobField__in=jobField, state__in=state)
    context['projects_progress'] = Project.objects.filter(user_jobField__owner=request.user.id, status=True, status_jobField_user=1).order_by('-id')
    context['laws'] = Group.objects.all()
    return render(request, 'client/dashboard.html', context)
