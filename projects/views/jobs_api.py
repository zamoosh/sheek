from .imports import *


def jobs_api(request):
    context = []
    for i in JobField.objects.filter(parent=None):
        context.append({'id': i.pk, 'title': i.title, 'description': i.description})
    return JsonResponse(context, safe=False)
