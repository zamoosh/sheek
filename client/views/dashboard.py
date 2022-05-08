from django.db.models import Q
from .imports import *

@login_required
def dashboard(request):
    context = {}
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/accounts/auth/")
    context['user_jobs'] = UserJobField.objects.filter(owner=request.user, status=True)
    context['laws'] = Group.objects.all()
    return render(request, 'client/dashboard.html',context)
