from .imports import *


def userjobfield(request):
    context = {}
    return render(request, 'project/userjob.html', context)
