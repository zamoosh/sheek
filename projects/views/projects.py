from .imports import *


def get_projects(request):
    context = {}
    context['expert_id'] = Project.objects.values_list('owner', flat=True).filter(owner=request.user.id)
    print(context['expert_id'])
    context['projects'] = User.objects.filter(id__in=context['expert_id'])
    print(context['projects'])
    return render(request, 'project/projects.html', context)
