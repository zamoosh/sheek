from .imports import *
from datetime import timedelta

@login_required
def userjob_api(request):
    context = []
    if request.is_ajax and request.method == "GET":
        jobField = request.GET.get('user_jobfield')
        state = State.objects.get(id=request.GET.get('state'))
        q = Q()
        q = q & Q(status=True, jobField=JobField.objects.get(id=jobField))
        experience = UserJobField.objects.filter(q)
        for item in experience:
            five_delta = datetime.date.today() - datetime.timedelta(days=1825)
            ten_delta = datetime.date.today() - datetime.timedelta(days=3650)
            if item.experience > five_delta:
                expert_id = UserJobField.objects.values_list('owner', flat=True).filter(q, owner=item.owner_id, state=state).distinct()
                expert = User.objects.filter(id__in=expert_id)
            elif item.experience > ten_delta:
                expert_id = UserJobField.objects.values_list('owner', flat=True).filter(q, owner=item.owner_id,
                                                                                        state__in=State.objects.filter(
                                                                                            parent_id=state.parent)).distinct()
                expert = User.objects.filter(id__in=expert_id)
            else:
                expert_id = UserJobField.objects.values_list('owner', flat=True).filter(q, owner=item.owner_id).distinct()
                expert = User.objects.filter(id__in=expert_id)
            for i in expert:
                context.append({'id': i.pk, 'name': i.first_name, 'last_name': i.last_name, 'birthday': i.birthday})
        return JsonResponse(context, safe=False)

