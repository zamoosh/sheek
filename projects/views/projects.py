from .imports import *


def get_projects(request):
    context = {}
    context['projects'] = Project.objects.filter(owner_id=request.user.id, status=True).order_by('-created_at')
    return render(request, 'project/projects.html', context)


def get_expert_projects(request):
    context = {}
    context['projects'] = Project.objects.filter(user_jobField__owner=request.user.id, status=True).order_by(
        '-created_at')
    return render(request, 'project/expert-projects.html', context)


def confirm_project(request, id):
    context = {}
    context['project'] = Project.objects.get(id=id)
    context['project'].status_jobField_user = 1
    context['project'].save()
    context['result'] = True
    return render(request, 'project/projects.html', context)


def reject_project(request, id):
    context = {}
    context['project'] = Project.objects.get(id=id)
    context['project'].status = False
    context['project'].save()
    context['dellresult'] = True
    message = Message()
    message.text = "پروژه شما توسط کارشناس رد شده است."
    message.project = Project.objects.get(id=id)
    message.owner_id = request.user.id
    message.save()
    return HttpResponseRedirect(reverse('projects:projects'))


def end_project(request, id):
    context = {}
    context['project_details'] = Project.objects.get(id=id)
    context['project'] = Project.objects.get(id=id)
    context['project'].status_jobField_user = 2
    context['project'].save()
    message = Message()
    message.text = "پروژه شما به اتمام رسید."
    message.project = Project.objects.get(id=id)
    message.owner_id = request.user.id
    message.save()
    return HttpResponseRedirect(reverse('projects:projects'))
