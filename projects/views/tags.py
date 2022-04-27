from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .imports import *


def tags(request):
    context = {}
    context['tags'] = Tag.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(context['tags'], 100)
    try:
        context['tags'] = paginator.page(page)
    except PageNotAnInteger:
        context['tags'] = paginator.page(1)
    except EmptyPage:
        context['tags'] = paginator.page(paginator.num_pages)
    if request.method == "POST":
        title = request.POST.get('tag', '').strip()
        tag = Tag(title=title)
        tag.save()
    return render(request, 'project/tags.html', context)
