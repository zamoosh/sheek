from django.urls import reverse

from .imports import *


def admins(request):
    context = {}
    if request.user.is_superuser:
        context['admins'] = User.objects.filter(is_superuser=True)
    else:
        HttpResponseRedirect(reverse('client:dashboard'))
    return render(request, 'client/admin_list.html', context)
