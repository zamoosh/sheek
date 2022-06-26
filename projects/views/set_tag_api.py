from .imports import *


def set_tag_api(request, pk):
    context = []
    tagin = Tag.get_tag(JobField.objects.get(id=pk))
    if request.is_ajax and request.method == "GET":
        q = Q(title__contains=request.GET.get('title'))
        for i in Tag.objects.filter(q):
            context.append({'id': i.id, 'title': i.title, 'checked': i in tagin})
    return JsonResponse(context, safe=False)
