from . import complaints
from .imports import *


def set_tags(request):
    context = {}
    context['salahiats'] = JobField.objects.filter(competence=True)
    return render(request, 'project/set_tags.html', context)
