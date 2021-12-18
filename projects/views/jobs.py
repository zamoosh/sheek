from .imports import *

@login_required
def jobs(request):
    context = {}
    try:
        context['jobs'] = JobField.objects.filter(status=True)
    except:
        pass
    if request.method == "POST":
        context['req'] = {}
        context['req']['title'] = request.POST.get('title', '').strip()
        context['req']['description'] = request.POST.get('description', '').strip()
        context['req']['parent'] = int(request.POST.get('parent'))
        job = JobField()
        job.title = context['req']['title']
        if context['req']['parent']:
            job.parent_id = context['req']['parent']
        job.save()
    return render(request, 'job/jobs.html', context)


def delete_job(request, id):
    context = {'job': JobField.objects.get(id=id)}
    context['job'].delete()
    return HttpResponseRedirect(reverse('projects:jobs'))
