from .imports import *


def addproject(request):
    context = {}
    # if request.method == "POST":
    #     context['req'] = {}
    #     context['req']['state'] = int(request.POST.get('city'))
    #     context['req']['expert'] = int(request.POST.get('subexpert'))
    #     context['req']['experience'] = request.POST.get('experience')
    #     userjobfield = UserJobField()
    #     userjobfield.state_id = context['req']['state']
    #     userjobfield.jobField_id = context['req']['expert']
    #     userjobfield.owner_id = request.user.id
    #     if request.POST.get('experience'):
    #         userjobfield.experience = jdatetime.datetime.strptime(request.POST.get('experience'), "%Y/%m/%d").togregorian()
    #     userjobfield.save()
    #     return HttpResponseRedirect(reverse('projects:userjob'))
    return render(request, 'project/addproject.html', context)