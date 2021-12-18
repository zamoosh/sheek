from .imports import *


def adduserjobfield(request):
    context = {}
    return render(request, 'project/add-userjob.html', context)
