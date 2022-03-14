from .imports import *


@login_required
def userjob_api(request):
    context = []
    if request.is_ajax and request.method == "GET":
        q = Q()
        jobField = request.GET.get('salahiat')
        state = request.GET.get('city')
        print(state)
        print(jobField)
        q = q & Q(status=True, jobField=jobField)

        user_state = UserState.objects.values_list('userjobfield_id', flat=True).filter(state=state, userjobfield__in=UserJobField.objects.filter(q))
        print(user_state)
        users = UserJobField.objects.values_list('owner', flat=True).filter(id__in=user_state)
        user = User.objects.filter(id__in=users)
        for i in user:
            tmp = {'id': i.pk, 'name': i.first_name, 'last_name': i.last_name, 'birthday': i.birthday }
            if i.image:
                tmp['profile'] = i.image.url
            context.append(tmp)
        return JsonResponse(context, safe=False)
