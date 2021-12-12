from .imports import *


def dashboard(request):
    return render(request, 'client/dashboard.html')
