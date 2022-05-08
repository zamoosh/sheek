from .imports import *


def expert_profile(request, id):
    context = {}
    context['user'] = User.objects.get(id=id)
    context['userJob'] = UserJobField.objects.filter(owner=context['user'])
    context['projects_done'] = Project.objects.filter(user_jobField__owner=context['user'], status_jobField_user=2)
    context['projects_inprog'] = Project.objects.filter(user_jobField__owner=context['user'], status_jobField_user=1)
    context['projects_before'] = Project.objects.filter(user_jobField__owner=context['user'], status_jobField_user=0)
    return render(request, 'project/expert_profile.html', context)
