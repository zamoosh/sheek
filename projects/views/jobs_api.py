from .imports import *

@login_required
def jobs_api(request, parent=None):
    context = []
    for i in JobField.objects.filter(parent=parent):
        context.append({'id': i.pk, 'title': i.title})
    return JsonResponse(context, safe=False)
