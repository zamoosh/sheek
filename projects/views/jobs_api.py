from .imports import *

from .imports import *


@login_required
def jobs_api(request, parent=None):
    context = []
    if request.is_ajax and request.method == "GET":
        for i in JobField.objects.filter(parent=parent):
            context.append({'id': i.pk, 'title': i.title})
    return JsonResponse(context, safe=False)


@login_required
def jobs_api_search(request, parent=None):
    context = []
    if request.is_ajax and request.method == "GET":
        job_field = Tag.objects.get(id=parent).jobfield.all()
        for i in job_field:
            context.append({'id': i.pk, 'title': i.title})
    return JsonResponse(context, safe=False)


@login_required
def jobs_api_search2(request, parent=None):
    context = {}
    if request.is_ajax and request.method == "GET":
        context['main'] = []
        context['main_parent'] = []
        job_field = JobField.objects.filter(parent=JobField.objects.get(id=parent).parent)
        print(job_field)
        context['select_parent_parent'] = job_field[0].parent.parent.id
        context['select_parent'] = job_field[0].parent.id
        context['selecte'] = parent
        for i in job_field:
            context['main'].append({'id': i.pk, 'title': i.title})
        for i in JobField.objects.filter(parent=JobField.objects.get(id=parent).parent.parent):
            context['main_parent'].append({'id': i.pk, 'title': i.title})

        # context['main_parent'] = []
        # job_field = JobField.objects.get(parent__parent=job_field)
        # for i in job_field:
        #     context['main_parent'].append({'id': i.pk, 'title': i.title})

    return JsonResponse(context, safe=False)
