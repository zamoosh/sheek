from . import complaints
from .imports import *


def set_tags(request):
    context = {}
    q = Q(competence=True)
    if request.method == 'POST':
        context['searchbar'] = request.POST.get('searchbar')
        q = q & Q(title__icontains=context['searchbar'])
    context['salahiats'] = JobField.objects.filter(q)
    return render(request, 'project/set_tags.html', context)
