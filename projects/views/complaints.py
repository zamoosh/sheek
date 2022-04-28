from .imports import *

def complaints(request):
    context = {}
    context['complaints'] = Complaint.objects.filter(project__in=Project.objects.filter(owner=request.user))
    print("asdasd")
    print("asdasd")
    print("asdasd")
    print("asdasd")
    return render(request, 'project/complaints.html', context)



