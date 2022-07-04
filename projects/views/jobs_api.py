from .import complaints
from .imports import *
from .imports import *


@login_required
def jobs_api(request, parent=None):
    context = []
    if request.is_ajax and request.method == "GET":
        for i in JobField.objects.filter(competence=False, parent=None, status=True).order_by('-id'):
            context.append({'id': i.pk, 'title': i.title, 'parent': i.parent_id})
    return JsonResponse(context, safe=False)


@login_required
def jobs_competence_api(request, parent=None):
    context = []
    if request.is_ajax and request.method == "GET":
        for item in JobField.objects.filter(~Q(parent=None), competence=False, status=True):
            child = JobField.get_child(item)
            if child:
                context.append({'id': child.pk, 'title': child.title, 'parent': child.parent_id})
    return JsonResponse(context, safe=False)


@login_required
def jobs_group_api(request, parent=None):
    context = []
    if request.is_ajax and request.method == "GET":
        for item in JobField.objects.filter(parent=parent, competence=False, status=True):
            child = JobField.get_child_competence(item)
            if child:
                context.append({'id': child.pk, 'title': child.title, 'parent': child.parent_id})
    return JsonResponse(context, safe=False)


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
        job_field = JobField.objects.filter(parent=JobField.objects.get(id=parent).parent, status=True)
        context['select_parent_parent'] = job_field[0].parent.parent.id
        context['select_parent'] = job_field[0].parent.id
        context['selecte'] = parent
        for i in job_field:
            context['main'].append({'id': i.pk, 'title': i.title})
        for i in JobField.objects.filter(parent=JobField.objects.get(id=parent).parent.parent, status=True):
            context['main_parent'].append({'id': i.pk, 'title': i.title})
    return JsonResponse(context, safe=False)


def adduser_jobs_api(request, id=None):
    context = []
    if request.is_ajax and request.method == "GET":
        for i in JobField.objects.filter(parent=id, status=True):
            context.append({'id': i.pk, 'title': i.title, 'competence': i.competence})
    return JsonResponse(context, safe=False)