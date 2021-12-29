from .imports import *


def addproject(request):
    context = {}
    if request.method == "POST":
        context['req'] = {}
        context['req']['state'] = int(request.POST.get('city'))
        context['req']['expert'] = int(request.POST.get('subexpert'))
        context['req']['title'] = request.POST.get('project-title', '').strip()
        context['req']['description'] = request.POST.get('project-description', '').strip()
        project = Project()
        project.state_id = context['req']['state']
        project.jobField_id = context['req']['expert']
        project.title = context['req']['title']
        project.description = context['req']['description']
        if request.POST.get('expert-list'):
            userjobfield = UserJobField.objects.get(owner=request.POST.get('expert-list')).id
            project.user_jobField_id = userjobfield
        project.owner_id = request.user.id
        project.save()
        if request.POST.get('expert-list'):
            message = Message()
            message.text = "شما یک درخواست دارید"
            message.project_id = project.id
            # message.owner_id = UserJobField.objects.get(owner=request.POST.get('expert-list')).id
            message.owner_id = request.POST.get('expert-list')
            message.save()
        return HttpResponseRedirect(reverse('projects:redierct'))
    return render(request, 'project/addproject.html', context)


def redierct(request):
    return render(request, 'project/project-done.html')
