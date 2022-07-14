from .imports import *


def api_sort_experts(request):
    context = {}
    experts = User.objects.filter(id__in=request.POST.getlist('ids')).annotate(total_rate=Sum('project__rate'), projects=Count('project'))
    expert_cities = experts.values_list('state__title', flat=True)
    city = State.objects.get(id=request.POST.get('city')).title
    sorting_key = request.POST.get('sorting')
    if 'city' in sorting_key:
        if city in list(expert_cities):
            experts_not_cities = experts.exclude(state__title__icontains=city)
            experts_have_cities = experts.filter(state__title__icontains=city)
            query = experts_have_cities | experts_not_cities
            # if 'close' in sorting_key:
            #     experts = experts.filter(q)
            # elif 'far' in sorting_key:
            #     experts = experts.exclude(q)
            # experts = a | b
            # experts = experts.distinct()
            context['experts'] = list(query.values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects'))
        else:
            context['experts'] = list(experts.values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects'))
    else:
        if sorting_key == 'more_score':
            context['experts'] = list(experts.order_by('-total_rate').values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects'))
        elif sorting_key == 'less_score':
            context['experts'] = list(experts.order_by('total_rate').values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects'))
    return JsonResponse(context, status=200)
