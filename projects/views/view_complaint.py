from .imports import *

def view_complaint(request, id, title):
    context = {}
    if Complaint.objects.filter(project__in=Project.objects.filter(owner=request.user)):
        context['complaint'] = Complaint.objects.get(id=id)
        context['texts'] = Text.objects.filter(complaint_id=id)
        if request.user.is_superuser:
            context['complaint'].type = 2
            context['complaint'].save()
        if request.method == "POST":
            text_comp = request.POST.get('complaint', '').strip()
            text = Text()
            text.owner = request.user
            text.complaint = Complaint.objects.get(id=id)
            text.text = text_comp
            text.save()
            context['complaint'].update_at = datetime.datetime.now()
            if request.user.is_superuser:
                context['complaint'].type = 3
            else:
                context['complaint'].type = 1
            context['complaint'].save()
    else:
        return HttpResponseRedirect(reverse('projects:complaints'))
    return render(request, 'project/view_complaint.html', context)


def end_complaint(request, id):
    context = {}
    complaint = Complaint.objects.get(id=id)
    complaint.status = 1
    complaint.save()
    context['end'] = True
    return HttpResponseRedirect(reverse('projects:complaints'))
