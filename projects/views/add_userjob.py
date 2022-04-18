from django.shortcuts import redirect
from .imports import *


@login_required
def adduserjobfield(request):
    context = {}
    context['old'] = UserJobField.objects.values('jobField').filter(owner=request.user)
    context['beold'] = JobField.objects.filter(jobfield__jobfield__in=context['old'], parent=None).distinct()
    context['jobfields'] = JobField.objects.filter(parent=None).exclude(jobfield__jobfield__in=context['old'])
    if request.method == 'POST':
        context['request'] = {}
        context['request']['expert-list'] = request.POST.get('expert-list')
        print('Conxt', context['request']['expert-list'])
        return HttpResponseRedirect(reverse('projects:adduser-jobs', args=[int(context['request']['expert-list'])]))
    return render(request, 'project/add-userjob.html', context)


def adduserjobfields(request, id):
    context = {'id': JobField.objects.get(id=id)}
    if request.method == "POST":
        context['jobfield'] = request.POST.getlist('jobfield')
        context['inquiry'] = request.POST.get('inquiry', '').strip()
        for i in context['jobfield']:
            if UserJobField.objects.filter(jobField=i, owner=request.user.id).exists():
                context['error'] = True
            else:
                userjobfield = UserJobField()
                userjobfield.owner_id = request.user.id
                userjobfield.jobField_id = i
                userjobfield.inquiry_link = context['inquiry']
                if request.POST.get('expiration'):
                    userjobfield.expiration = jdatetime.datetime.strptime(request.POST.get('expiration'),
                                                                          "%Y/%m/%d").togregorian()
                if request.POST.get('issue'):
                    userjobfield.issue = jdatetime.datetime.strptime(request.POST.get('issue'),
                                                                     "%Y/%m/%d").togregorian()
                if 'document_picture' in request.FILES:
                    userjobfield.document_image = request.FILES['document_picture']
                userjobfield.save()
        return HttpResponseRedirect(reverse('projects:userjob'))
    return render(request, 'project/add-userjob-field.html', context)
