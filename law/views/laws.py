from .imports import *


def laws(request):
    context = {}
    context['laws'] = Group.objects.all()
    return render(request, 'law/laws.html', context)
