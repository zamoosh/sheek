from .imports import *

def admin_complaints(request):
    context = {}
    context['complaints'] = Complaint.objects.all()
    return render(request, 'project/admin_complaints.html', context)



