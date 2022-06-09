from .imports import *


def set_tag(request, pk):
    context = {}
    context['salahiat'] = JobField.objects.get(id=pk)
    job = JobField.objects.get(id=pk)
    context['tags'] = Tag.objects.all()
    context['tagin'] = Tag.get_tag(context['salahiat'])
    if request.method == "POST":
        print(request.POST.getlist('tag'))
        selected_tags = Tag.objects.filter(id__in=request.POST.getlist('tag')).values_list('id', flat=True)
        common = job.tag_set.filter(id__in=selected_tags)
        common_ids = common.values_list('id', flat=True)
        delete = job.tag_set.filter(~Q(id__in=selected_tags))
        for item in delete:
            item.jobfield.remove(job)
        add = []
        for item in selected_tags:
            if not (item in common_ids):
                add.append(item)
        for item in add:
            job.tag_set.add(Tag.objects.get(id=item))
            job.save()
    return render(request, 'project/set_tag.html', context)
