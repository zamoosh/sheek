from .imports import *


def api_sort_experts(request):
    context = {}
    experts = User.objects.filter(id__in=request.POST.getlist('ids')).annotate(total_rate=Sum('project__rate'), projects=Count('project'))
    expert_cities = experts.values_list('state__title', flat=True)
    city = State.objects.get(id=request.POST.get('city'))
    sorting_key = request.POST.get('sorting')
    if ('city' in sorting_key) and (city in expert_cities):
        if sorting_key == 'clos_city':
            pass
        elif sorting_key == 'far_city':
            pass
    else:
        if sorting_key == 'more_score':
            context['experts'] = list(experts.order_by('-total_rate').values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects'))
        elif sorting_key == 'less_score':
            context['experts'] = list(experts.order_by('total_rate').values('id', 'first_name', 'last_name', 'birthday', 'image', 'projects'))
    return JsonResponse(context, status=200)
