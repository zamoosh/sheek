from .imports import *


def get_projects(request):
    context = {}
    # context['projects'] = Project.objects.values_list('owner', flat=True).filter(user_jobField__owner=request.user.id)
    context['projects'] = Project.objects.filter(user_jobField__owner=request.user.id)
    print(context['projects'])
    return render(request, 'project/projects.html', context)
