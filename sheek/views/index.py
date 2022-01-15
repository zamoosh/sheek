from .imports import *


def index(request):
    context = {}
    return render(request, 'site/index.html', context)
