from .imports import *

@login_required
def state_api(request, parent=None):
    context = []
    for i in State.objects.filter(parent=parent):
        context.append({'id': i.pk, 'title': i.title})
    return JsonResponse(context, safe=False)
