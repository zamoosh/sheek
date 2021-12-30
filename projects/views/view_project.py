from .imports import *


def view_project(request, id):
    context = {}
    context['project_details'] = Project.objects.get(id=id)
    return render(request, 'project/view_project.html', context)
