from .imports import *


def job_search(request):
    context = []
    if request.is_ajax and request.method == "GET":
        title = request.GET.get('title')
        for i in Tag.objects.filter(title__contains=title):
            context.append({'id': i.pk, 'title': i.title})
    return JsonResponse(context, safe=False)
