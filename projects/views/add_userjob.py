from django.shortcuts import redirect

from .imports import *


@login_required
def adduserjobfield(request):
    context = {}
    context['jobfields'] = JobField.objects.filter(parent=None)
    if request.method == 'POST':
        context['request'] = {}
        context['request']['expert-list'] = int(request.POST.get('expert-list'))
        return redirect(reverse('projects:adduser-jobs', args=(context['request']['expert-list'],)))
    return render(request, 'project/add-userjob.html', context)


def adduserjobfields(request, id):
    context = {}
    context['id'] = JobField.objects.get(id=id)

    # if request.method == "POST":
    #     context['req'] = {}
    #     context['req']['jobfield'] = request.POST.getlist('jobfield')
    #     print(context['req']['jobfield'])
    #     context['req']['inquiry'] = request.POST.get('inquiry', '').strip()
    #     for i in context['req']['jobfield']:
    #         if UserJobField.objects.filter(jobField=i, owner=request.user.id).exists():
    #             context['error'] = True
    #         else:
    #             userjobfield = UserJobField()
    #             userjobfield.owner_id = request.user.id
    #             userjobfield.jobField_id = i
    #             userjobfield.inquiry_link = context['req']['inquiry']
    #             if request.POST.get('expiration'):
    #                 userjobfield.expiration = jdatetime.datetime.strptime(request.POST.get('expiration'),
    #                                                                       "%Y/%m/%d").togregorian()
    #             if request.POST.get('issue'):
    #                 userjobfield.issue = jdatetime.datetime.strptime(request.POST.get('issue'),
    #                                                                  "%Y/%m/%d").togregorian()
    #             if 'document_picture' in request.FILES:
    #                 userjobfield.document_image = request.FILES['document_picture']
    #             userjobfield.save()
    #     return HttpResponseRedirect(reverse('projects:userjob'))
    return render(request, 'project/add-userjob-field.html', context)
