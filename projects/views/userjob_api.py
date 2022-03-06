from .imports import *


@login_required
def userjob_api(request):
    context = []
    if request.is_ajax and request.method == "GET":
        jobField = request.GET.get('salahiat')
        print(jobField)
        state = UserState.objects.filter(jobField_id=jobField)
        print(state)
        q = Q()
        q = q & Q(status=True, jobField=JobField.objects.get(id=jobField))
        experience = UserJobField.objects.filter(q)
        for item in experience:
            five_delta = datetime.date.today() - datetime.timedelta(days=1825)
            ten_delta = datetime.date.today() - datetime.timedelta(days=3650)
            if item.issue > five_delta:
                expert_id = UserJobField.objects.values_list('owner', flat=True).filter(q, owner=item.owner_id).distinct()
                expert = User.objects.filter(id__in=expert_id)
            elif item.issue > ten_delta:
                expert_id = UserJobField.objects.values_list('owner', flat=True).filter(q, owner=item.owner_id).distinct()
                expert = User.objects.filter(id__in=expert_id)
            else:
                expert_id = UserJobField.objects.values_list('owner', flat=True).filter(q, owner=item.owner_id).distinct()
                expert = User.objects.filter(id__in=expert_id)
            for i in expert:
                tmp = {'id': i.pk, 'name': i.first_name, 'last_name': i.last_name, 'birthday': i.birthday}
                if i.image:
                    tmp['profile'] = i.image.url
                context.append(tmp)
        return JsonResponse(context, safe=False)
