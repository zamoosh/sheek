from .imports import *


def laws(request, id):
    context = {}
    context['laws'] = Rule.objects.filter(group=id)
    return render(request, 'law/laws.html', context)
