from django.urls import reverse
from .imports import *


def expert_request(request):
    context = {}
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        user.has_jobField = True
        if 'national-card' in request.FILES:
            user.national_card = request.FILES['national-card']
        user.save()
        return HttpResponseRedirect(reverse('projects:adduserjob'))
    return render(request, 'client/expert_request.html', context)
