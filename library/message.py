from django.db.models import Q

from projects.models import *


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            projects = Project.objects.filter(Q(owner=request.user) | Q(user_jobField__owner=request.user))
            q = Q()
            q = q & Q(Q(user_view=False) | Q(expert_view=False))
            message = []
            message = Message.objects.filter(q & ~Q(owner=request.user), project__in=projects)
            request.message = message
            response = self.get_response(request)
            return response
