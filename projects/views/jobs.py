from .imports import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def jobs(request):
    context = {}
    q = Q(status=True)
    if request.method == 'POST':
        context['searchbar'] = request.POST.get('searchbar')
        q = q & Q(title__icontains=context['searchbar'])
    context['jobs'] = JobField.objects.filter(q).order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(context['jobs'], 50)
    try:
        context['jobs'] = paginator.page(page)
    except PageNotAnInteger:
        context['jobs'] = paginator.page(1)
    except EmptyPage:
        context['jobs'] = paginator.page(paginator.num_pages)
    if request.method == "POST":
        context['req'] = {}
        context['req']['subgroup'] = request.POST.get('subgroup')
        context['req']['group'] = request.POST.get('group')
        context['req']['competence'] = request.POST.get('competence')
        context['req']['title'] = request.POST.get('job', '').strip()
        context['req']['description'] = request.POST.get('description', '').strip()
        context['req']['parent'] = request.POST.get('parent')
        if context['req']['subgroup']:
            job = JobField()
            job.title = context['req']['title']
            job.save()
        if context['req']['group']:
            job = JobField()
            job.title = context['req']['title']
            if context['req']['parent']:
                job.parent_id = int(context['req']['parent'])
            job.save()
        if context['req']['competence']:
            job = JobField()
            job.title = context['req']['title']
            if context['req']['parent']:
                job.parent_id = int(context['req']['parent'])
            job.competence = True
            job.save()
    return render(request, 'project/jobs.html', context)


def delete_job(request, id):
    context = {'job': JobField.objects.get(id=id)}
    context['job'].delete()
    return HttpResponseRedirect(reverse('projects:jobs'))
