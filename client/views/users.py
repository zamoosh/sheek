from django.db.models import Q
from django.urls import reverse

from .imports import *


def users(request):
    context = {}
    if request.user.is_superuser:
        context['admins'] = User.objects.filter(~Q(is_superuser=True), ~Q(has_jobField=True))
    else:
        HttpResponseRedirect(reverse('client:dashboard'))
    if request.method == "POST":
        context['searchbar'] = request.POST.get('searchbar', '')
        context['admins'] = User.objects.filter(has_jobField=True, cellphone__icontains=context['searchbar'])
    return render(request, 'client/user_list.html', context)


def users_admins(request, id):
    context = {}

    if request.method == "POST":
        context['req'] = {}
        context['req']['first_name'] = request.POST.get('first_name', '').strip()
        context['req']['last_name'] = request.POST.get('last_name', '').strip()
        context['req']['email'] = request.POST.get('email', '').strip()
        context['req']['status'] = int(request.POST.get('status'))
        context['req']['role'] = int(request.POST.get('role'))
        user = User.objects.get(id=id)
        user.first_name = context['req']['first_name']
        user.last_name = context['req']['last_name']
        user.email = context['req']['email']

        if context['req']['status'] == 2:
            user.is_active = False
        elif context['req']['status'] == 1:
            user.is_active = True

        if context['req']['role'] == 1:
            user.is_superuser = False
        elif context['req']['role'] == 2:
            user.is_superuser = True

        user.save()
    context['user'] = User.objects.get(id=id)
    return render(request, 'client/edit_user.html', context)
