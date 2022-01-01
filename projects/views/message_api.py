from .imports import *


def message_api(request, id):
    context = {}
    print("sdsdfsdf")
    if request.is_ajax and request.method == "POST":
        print("sdsdfsdf")
        context['project_details'] = Project.objects.get(id=id)
        context['req'] = {}
        context['req']['messageText'] = request.POST.get('messageText', '').strip()
        message = Message()
        message.text = context['req']['messageText']
        message.owner_id = request.user.id
        message.project = Project.objects.get(id=id)
        message.save()
        # message.text = "کارشناس برای شما یک پیام ارسال کرده است"
        # message.owner_id = 0
        # message.project = Project.objects.get(id=id)
        # message.save()
    return render(request, 'project/view_project.html', context)