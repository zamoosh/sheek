from django.core.exceptions import ObjectDoesNotExist
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
        context['req']['linkedin'] = request.POST.get('linkedin', '').strip()
        context['req']['instagram'] = request.POST.get('instagram', '').strip()
        context['req']['whatsapp'] = request.POST.get('whatsapp', '').strip()
        context['req']['telegram'] = request.POST.get('telegram', '').strip()
        context['req']['gender'] = request.POST.get('gender', '').strip()
        user = User.objects.get(id=request.user.id)
        user.first_name = context['req']['first_name']
        user.last_name = context['req']['last_name']
        user.email = context['req']['email']
        # try:
        #     user_national = User.objects.get(national_code=context['req']['national_code'])
        #     context['error'] = True
        #     print('no1')
        # except ObjectDoesNotExist:
        user.national_code = context['req']['national_code']
        print('ok1')
        user.extra['linkedin'] = context['req']['linkedin']
        user.extra['instagram'] = context['req']['instagram']
        user.extra['whatsapp'] = context['req']['whatsapp']
        user.extra['telegram'] = context['req']['telegram']
        if context['req']['gender'] == "male":
            user.gender = 1
        elif context['req']['gender'] == "female":
            user.gender = 0
        if request.POST.get('birthday'):
            user.birthday = jdatetime.datetime.strptime(request.POST.get('birthday'), "%Y/%m/%d").togregorian()
        # request.user.state = context['req']['state']
        if request.POST.get('state'):
            user.state_id = int(request.POST.get('state'))
        if 'profile-picture' in request.FILES:
            user.image = request.FILES['profile-picture']
        if 'error' not in context:
            user.save()
        return HttpResponseRedirect(reverse('client:profile'))
    return render(request, 'client/profile.html', context)