from django.shortcuts import render


def state(request):
    context = {}
    return render(request, 'state/states.html', context)
