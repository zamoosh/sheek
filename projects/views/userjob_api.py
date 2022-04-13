from .imports import *


@login_required
def userjob_api(request):
    context = []
    if request.is_ajax and request.method == "GET":
        q = Q()
        jobField = request.GET.get('salahiat')
        state = request.GET.get('city')
        q = q & Q(status=True, jobField=jobField)

        user_state = UserState.objects.values_list('userjobfield_id', flat=True).filter(state=state, userjobfield__in=UserJobField.objects.filter(q))
        print(user_state)
        users = UserJobField.objects.values_list('owner', flat=True).filter(id__in=user_state)
        user = User.objects.filter(id__in=users)
        for i in user:
            user_jobs = len(Project.objects.filter(user_jobField__owner=i.pk))
            tmp = {'id': i.pk, 'name': i.first_name, 'last_name': i.last_name, 'birthday': i.birthday }
            if i.image:
                tmp['profile'] = i.image.url
            tmp['projects'] = user_jobs
            context.append(tmp)
        return JsonResponse(context, safe=False)
