from .imports import *


def view_project(request, id):
    context = {}
    if Project.objects.filter(user_jobField__owner_id=request.user.id, id=id):
        context['project_details'] = Project.objects.get(id=id)
        context['reports'] = Report.objects.filter(project_id=id).order_by('-created_at')
    else:
        context['msg'] = "Dont access!"
        return render(request, 'authorized.html', context)
    return render(request, 'project/view_project.html', context)
