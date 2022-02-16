from .imports import *


def index(request):
    return redirect('/accounts/dashboard/')
    # context = {}
    # return render(request, 'site/index.html', context)
