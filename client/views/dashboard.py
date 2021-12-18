from .imports import *

@login_required
def dashboard(request):
    return render(request, 'client/dashboard.html')
