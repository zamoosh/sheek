from .imports import *

def projects_api(request):
    context = []
    if request.is_ajax and request.method == "GET":
        for i in Project.objects.filter(owner=request.user.id, status=True):
            context.append({'id': i.pk, 'title': i.title})
    return JsonResponse(context, safe=False)

def add_complaint(request):
    context = {}
    if request.method == "POST":
        title = request.POST.get('title', '').strip()
        project = int(request.POST.get('project'))
        text_complaint = request.POST.get('complaint', '').strip()
        complaint = Complaint()
        complaint.title = title
        complaint.project = Project.objects.get(id=project)
        complaint.type = 1
        complaint.save()
        text = Text()
        text.owner_id = request.user.id
        text.complaint_id = complaint.id
        text.text = text_complaint
        text.save()
        return HttpResponseRedirect(reverse('projects:complaints'))
    return render(request, 'project/add-complaint.html', context)



