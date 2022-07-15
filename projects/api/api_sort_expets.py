import numpy as np

from .imports import *


def api_sort_experts(request):
    context = {}
    experts = User.objects.filter(id__in=request.POST.getlist('ids')).annotate(total_rate=Sum('project__rate'), projects=Count('project'))
    expert_cities = experts.values_list('state__title', flat=True)
    city = State.objects.get(id=request.POST.get('city')).title
    sorting_key = request.POST.get('sorting')
    if 'city' in sorting_key:  # filter by city
        if city in list(expert_cities):  # if searched city was in experts city
            if 'close' in sorting_key:  # sort by closest city
                sorted_experts = np.array(experts.filter(state__title__icontains=city).values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects'), dtype=QuerySet)
                sorted_experts = np.append(sorted_experts, np.array(experts.exclude(state__title__icontains=city).values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects')))
            else:  # sort by farthest city
                sorted_experts = np.array(experts.filter(state__title__icontains=city).values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects'), dtype=QuerySet)
                sorted_experts = np.append(sorted_experts, np.array(experts.exclude(state__title__icontains=city).values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects')))
            context['experts'] = sorted_experts.tolist()
        else:  # if the searched city wasn't in experts city
            context['experts'] = list(experts.values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects'))
    else:  # filter by score(rate)
        if sorting_key == 'more_score':
            context['experts'] = list(experts.order_by('-total_rate').values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects'))
        elif sorting_key == 'less_score':
            context['experts'] = list(experts.order_by('total_rate').values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects'))
    return JsonResponse(context, status=200)
