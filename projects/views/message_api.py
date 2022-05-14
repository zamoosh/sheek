from .imports import *

@login_required
def message_api(request, id):
    context = {}
    if request.is_ajax and request.method == "POST":
        print("ASDADASDASDASDSD")
        context['project_details'] = Project.objects.get(id=id)
        context['req'] = {}
        context['req']['messageText'] = request.POST.get('messageText', '').strip()
        message = Message()
        message.text = context['req']['messageText']
        message.owner_id = context['project_details'].user_jobField.owner_id
        message.project = Project.objects.get(id=id)
        message.save()
        message.text = "کارشناس برای شما یک پیام ارسال کرده است"
        # message.owner_id = 0
        # message.project = Project.objects.get(id=id)
        # message.save()
    return render(request, 'project/view_project.html', context)


def setreadmessage(request, id):
    context = {}
    context['getReadMesseage'] = Message.objects.filter(project=id)
    for i in context['getReadMesseage']:
        if request.user.id == i.project.owner_id:
            i.user_view = True
            i.save()
        elif request.user.id == i.project.user_jobField.owner_id:
            i.expert_view = True
            i.save()
    return render(request, 'project/view_project.html', context)
