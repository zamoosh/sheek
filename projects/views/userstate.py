from django.shortcuts import redirect

from .imports import *


@login_required
def userstate(request):
    context = {}
    context['userJobFields'] = UserJobField.objects.filter(status=True, owner=request.user.id).order_by('-id')
    for i in context['userJobFields']:
        context['userstate'] = UserState.objects.filter(userjobfield=i.pk)
    return render(request, 'project/userstate.html', context)


@login_required
def adduserstate(request, id):
    context = {}
    print('1')
    context['getJobField'] = UserJobField.objects.get(id=id)
    q = Q()
    q = q & Q(status=True, jobField=UserJobField.objects.get(id=id).jobField)
    five_delta = datetime.date.today() - datetime.timedelta(days=5 * 365)
    ten_delta = datetime.date.today() - datetime.timedelta(days=10 * 365)
    experience_five = UserJobField.objects.filter(q, owner=request.user.id, issue__gte=five_delta)
    experience_ten = UserJobField.objects.filter(q, owner=request.user.id, issue__lt=five_delta,
                                                 issue__gte=ten_delta)
    experience_full = UserJobField.objects.filter(q, owner=request.user.id, issue__lte=ten_delta)
    if experience_five:
        context['experience_five'] = True
    if experience_ten:
        context['experience_ten'] = True
    if experience_full:
        context['experience_full'] = True
    if request.method == "POST":
        context['userstate'] = request.POST.getlist('userstate')
        print(context['userstate'])
        user_states_selected = []
        u = User.objects.get(id=request.user.id)
        for userjobfield in u.userjobfield_set.all():
            for userstate in userjobfield.userstate_set.all():
                user_states_selected.append(userstate.state.title)
        states = State.objects.filter(id__in=context['userstate']).values_list('title', flat=True)
        for s in states:
            if s not in user_states_selected:
                user_state = UserState()
                user_state.userjobfield_id = id
                user_state.state_id = State.objects.get(title=s, parent__id=request.POST.get('state')).id
                user_state.save()
        context['save'] = True
    return render(request, 'project/add-userstate.html', context)


@login_required
def userstateapi(request, id):
    context = {}
    state_list = []
    if request.method == "GET":
        print("aaaa")
        expert_list = []
        q = Q()
        q = q & Q(status=True, jobField=UserJobField.objects.get(id=id).jobField)
        state = request.user.state
        five_delta = datetime.date.today() - datetime.timedelta(days=5 * 365)
        ten_delta = datetime.date.today() - datetime.timedelta(days=10 * 365)
        experience_ten = UserJobField.objects.filter(q, owner=request.user.id, issue__lt=five_delta,
                                                     issue__gte=ten_delta)
        if experience_ten:
            state_li = []
            user_history_proj = UserState.objects.filter(userjobfield=id)
            for i in user_history_proj:
                state_li.append(i.state.id)
            user_ten = State.objects.filter(parent=state.parent).exclude(id__in=state_li)
            expert_list += user_ten
        for i in expert_list:
            state_list.append({'id': i.pk, 'title': i.title})
    return JsonResponse(state_list, safe=False)


@login_required
def dellstate(request, id):
    rm = UserState.objects.get(id=id)
    job_id = rm.userjobfield_id
    print(job_id)
    rm.delete()
    return redirect(reverse('projects:adduserstate', args=(job_id,)))

@login_required
def get_userstateapi(request, id):
    state_list = []
    if request.method == "GET":
        user_state = UserState.objects.filter(userjobfield=id)
        for i in user_state:
            state_list.append({'id': i.pk, 'title': i.state.title, 'parent_id': i.state_id})
    return JsonResponse(state_list, safe=False)
