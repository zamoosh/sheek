from .imports import *

@login_required
def get_projects(request):
    context = {}
    context['projects_start'] = Project.objects.filter(owner_id=request.user.id, status=True, status_jobField_user=0).order_by('-created_at')
    context['projects_progress'] = Project.objects.filter(owner_id=request.user.id, status=True, status_jobField_user=1).order_by('-created_at')
    context['projects_done'] = Project.objects.filter(owner_id=request.user.id, status=True, status_jobField_user=2).order_by('-created_at')
    return render(request, 'project/projects.html', context)

@login_required
def get_expert_projects(request):
    context = {}
    if 'confirm' in request.GET:
        context['project'] = Project.objects.get(id=int(request.GET.get('confirm')))
        if context['project'].status_jobField_user == 0:
            context['project'].status_jobField_user = 1
            context['project'].save()
            context['result'] = True
    context['projects_start'] = Project.objects.filter(user_jobField__owner=request.user.id, status=True, status_jobField_user=0).order_by(
        '-id')
    context['projects_progress'] = Project.objects.filter(user_jobField__owner=request.user.id, status=True, status_jobField_user=1).order_by(
        '-id')
    context['projects_done'] = Project.objects.filter(user_jobField__owner=request.user.id, status=True, status_jobField_user=2).order_by(
        '-id')
    return render(request, 'project/expert-projects.html', context)

@login_required
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

@login_required
def end_project(request, id):
    if request.method == "POST":
        context = {}
        context['rate'] = request.POST.get('rating')
        context['rate_description'] = request.POST.get('rate_description')
        context['project_details'] = Project.objects.get(id=id)
        context['project'] = Project.objects.get(id=id)
        context['project'].status_jobField_user = 2
        context['project'].rate = context['rate']
        context['project'].save()
        context['comment'] = Comment()
        context['comment'].projects_id = id
        context['comment'].text = context['rate_description']
        context['comment'].save()
        message = Message()
        message.text = "پروژه توسط کاربر اعلام اتمام شد."
        message.project = context['project_details']
        message.owner_id = context['project_details'].user_jobField.owner_id
        message.save()
    return HttpResponseRedirect(reverse('projects:expert-projects'))
