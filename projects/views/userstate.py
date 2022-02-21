from .imports import *


@login_required
def userstate(request):
    context = {}
    context['userJobFields'] = UserJobField.objects.filter(status=True)
    for i in context['userJobFields']:
        context['userstate'] = UserState.objects.filter(jobField_id=i.pk)
    return render(request, 'project/userstate.html', context)


@login_required
def adduserstate(request, id):
    context = {}
    context['getJobField'] = JobField.objects.get(id=id)
    q = Q()
    q = q & Q(status=True, jobField=JobField.objects.get(id=id))
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
        for i in context['userstate']:
            user_state = UserState()
            user_state.jobField_id = id
            user_state.owner_id = request.user.id
            user_state.state_id = i
            user_state.save()
    return render(request, 'project/add-userstate.html', context)


@login_required
def userstateapi(request, id):
    context = {}
    state_list = []
    if request.method == "GET":
        expert_list = []
        q = Q()
        q = q & Q(status=True, jobField=JobField.objects.get(id=id))
        state = request.user.state
        five_delta = datetime.date.today() - datetime.timedelta(days=5 * 365)
        ten_delta = datetime.date.today() - datetime.timedelta(days=10 * 365)
        experience_ten = UserJobField.objects.filter(q, owner=request.user.id, issue__lt=five_delta,
                                                     issue__gte=ten_delta)
        if experience_ten:
            user_ten = State.objects.filter(parent=state.parent)
            expert_list += user_ten
        for i in expert_list:
            state_list.append({'id': i.pk, 'title': i.title})
    return JsonResponse(state_list, safe=False)


@login_required
def get_userstateapi(request, id):
    state_list = []
    if request.method == "GET":
        user_state = UserState.objects.filter(jobField=id)
        for i in user_state:
            state_list.append({'id': i.pk, 'title': i.state.title})
    return JsonResponse(state_list, safe=False)
