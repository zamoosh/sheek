from django.urls import reverse

from .imports import *


def register_user(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get('first_name', '')
        lname = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        cellphone = request.POST.get('cellphone', '')
        user = User.objects.create_user(
            cellphone=cellphone,
            username=cellphone
        )
        user.first_name = name
        user.last_name = lname
        user.email = email
        user.is_superuser = True
        user.save()
        return HttpResponseRedirect(reverse('client:admins'))
    return render(request, 'client/register-user.html', context)
