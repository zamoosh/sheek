from .imports import *


def set_tag_toggle_api(request, pk, tpk):
    context = {}
    status = [False]
    if request.is_ajax and request.method == "GET":
        context['salahiat'] = JobField.objects.get(id=pk)
        job = JobField.objects.get(id=pk)
        context['tagin'] = Tag.get_tag(context['salahiat'])
        context['tag'] = Tag.objects.get(id=tpk)
        if context['tag'] in context['tagin']:
            context['tag'].jobfield.remove(job)
        else:
            job.tag_set.add(context['tag'])
            status[0] = True
    return JsonResponse(status, safe=False)
