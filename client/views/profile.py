from django.urls import reverse
from .imports import *
import jdatetime

@login_required
def profile(request):
    context = {}
    if request.method == "POST":
        context['req'] = {}
        context['req']['first_name'] = request.POST.get('first_name', '').strip()
        context['req']['last_name'] = request.POST.get('last_name', '').strip()
        context['req']['email'] = request.POST.get('email', '').strip()
        context['req']['national_code'] = request.POST.get('national_code', '').strip()
        context['req']['gender'] = request.POST.get('gender', '').strip()
        context['req']['state'] = int(request.POST.get('state'))
        user = User.objects.get(id=request.user.id)
        user.first_name = context['req']['first_name']
        user.last_name = context['req']['last_name']
        user.email = context['req']['email']
        user.national_code = context['req']['national_code']
        if context['req']['gender'] == "male":
            user.gender = 1
        elif context['req']['gender'] == "female":
            user.gender = 0
        if request.POST.get('birthday'):
            user.birthday = jdatetime.datetime.strptime(request.POST.get('birthday'), "%Y/%m/%d").togregorian()
        # request.user.state = context['req']['state']
        user.state_id = request.POST.get('state')
        user.save()
        return HttpResponseRedirect(reverse('client:profile'))
    return render(request, 'client/profile.html', context)
