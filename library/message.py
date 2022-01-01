from projects.models import *

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        message = Message.objects.filter(owner=request.user.id).order_by('-created_at')
        request.message = message
        response = self.get_response(request)
        return response
