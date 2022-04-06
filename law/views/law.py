from .imports import *


def law(request, id):
    context = {}
    context['group'] = Group.objects.get(id=id)
    context['laws'] = Group.objects.all()
    context['lawsAcardeon'] = Rule.objects.filter(group=id)
    if request.method == "POST":
        context['searchbar'] = request.POST.get('searchbar')
        context['lawsAcardeon'] = Rule.objects.filter(title__icontains=context['searchbar'])
        context['lawsAcardeon'] = Rule.objects.filter(title__icontains=context['searchbar'])
        context['lawsAcardeon'] = Rule.objects.filter(description__icontains=context['searchbar'])
    return render(request, 'law/laws.html', context)
