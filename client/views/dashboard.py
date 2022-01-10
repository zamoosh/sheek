from .imports import *

@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/accounts/auth/")
    return render(request, 'client/dashboard.html')
