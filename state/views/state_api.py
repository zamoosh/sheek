from .imports import *


def state_api(request):
    context = []
    for i in State.objects.filter(parent=None):
        context.append({'id': i.pk, 'title': i.title})
    return JsonResponse(context,safe=False)
