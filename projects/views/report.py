from .imports import *

@login_required
def report_api(request, id):
    context = {}
    if request.is_ajax and request.method == "POST":
        context['project_details'] = Project.objects.get(id=id)
        context['req'] = {}
        context['req']['title'] = request.POST.get('reportTitle', '').strip()
        context['req']['description'] = request.POST.get('reportDescription', '').strip()
        reports = Report()
        reports.title = context['req']['title']
        reports.description = context['req']['description']
        reports.project = Project.objects.get(id=id)
        reports.save()
        message = Message()
        expert = context['project_details'].user_jobField.owner_id
        message.text = "کارشناس برای شما یک گزارش ایجاد کرده است"
        message.owner_id = expert
        message.project = Project.objects.get(id=id)
        message.save()
    return render(request, 'project/view_project.html', context)

