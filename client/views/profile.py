from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib import messages
from .imports import *
import jdatetime
from django.db.models import Q


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
        context['req']['existential'] = request.POST.get('existential')
        request.user.first_name = context['req']['first_name']
        request.user.last_name = context['req']['last_name']
        request.user.email = context['req']['email']
        try:
            q = Q(national_code=context['req']['national_code']) & ~Q(id=request.user.id)
            user_national = User.objects.get(q)
            context['error'] = True
            messages.error(request, 'کد ملی تکراری می باشد.')
        except ObjectDoesNotExist:
            request.user.national_code = context['req']['national_code']
        request.user.extra['linkedin'] = context['req']['linkedin']
        request.user.extra['instagram'] = context['req']['instagram']
        request.user.extra['whatsapp'] = context['req']['whatsapp']
        request.user.extra['telegram'] = context['req']['telegram']
        if context['req']['gender'] == "male":
            request.user.gender = 1
        elif context['req']['gender'] == "female":
            request.user.gender = 0
        if request.POST.get('birthday'):
            request.user.birthday = jdatetime.datetime.strptime(request.POST.get('birthday'), "%Y/%m/%d").togregorian()
        if request.POST.get('city'):
            request.user.state_id = int(request.POST.get('city'))
        if 'profile-picture' in request.FILES:
            request.user.image = request.FILES['profile-picture']
        if context['req']['existential'] == "realperson":
            request.user.existential = False
        if context['req']['existential'] == "legalperson":
            request.user.existential = True
        if 'error' not in context:
            request.user.save()
    return render(request, 'client/profile.html', context)
