from .imports import *

def state(request):
    context = {}
    try:
        context['states'] = State.objects.all()
    except:
        pass
    if request.method == "POST":
        context['req'] = {}
        context['req']['city'] = request.POST.get('city', '').strip()
        context['req']['parent'] = int(request.POST.get('parent'))
        city = State()
        city.title = context['req']['city']
        if context['req']['parent']:
            city.parent_id = context['req']['parent']
        city.save()
    return render(request, 'state/states.html', context)
