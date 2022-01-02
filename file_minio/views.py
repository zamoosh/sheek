from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from .models import File as File_minio
import os
from django.conf import settings


# Create your views here.
def create_key(request):
    if request.method == 'GET':
        data = {}
        q = Q(name=request.GET.get('file_name'))
        q = q & Q(owner=request.user)
        # q = q & Q(extra__type=request.GET.get('type'))
        # q = q & Q(extra__id=request.GET.get('id'))
        q = q & Q(extra__size=request.GET.get('size'))
        q = q & ~Q(extra__contains='move')
        if File_minio.objects.filter(q).exists():
            file = File_minio.objects.get(q)
        else:
            file = File_minio()
            file.name = request.GET.get('file_name')
            # file.extra['type'] = request.GET.get('type')
            # file.extra['id'] = request.GET.get('id')
            file.extra['size'] = request.GET.get('size')
            file.owner = request.user
            file.save()
        data['key'] = file.key
        return JsonResponse(data)


def chunk_upload(request):
    context = {}
    context['msg'] = 'OK'
    if request.method == 'POST':
        key = request.data.get('key', None)
        if key:
            q = Q(key=key, owner=request.user)
            q = q & ~Q(extra__contains='move')
            file = File_minio.objects.get(q)
            file_path = os.path.join(settings.MEDIA_ROOT, 'tmp', str(file.owner.id))
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            file_path = os.path.join(file_path, file.name)
            if 'file' in request.FILES:
                upload = request.FILES['file']
                if os.path.exists(file_path):
                    with open(file_path, 'ba') as f:
                        f.write(request.FILES['file'].read())
                else:
                    with open(file_path, 'wb') as f:
                        f.write(request.FILES['file'].read())
            if os.path.exists(file_path):
                context['size'] = os.path.getsize(file_path)
                try:
                    context['step'] = os.path.getsize(file_path) / int(request.data.get('chunk_size', None))
                except:
                    pass
                context['percentage'] = os.path.getsize(file_path) / int(file.extra['size']) * 100
                if str(file.extra['size']) == str(context['size']):
                    file.extra['status'] = True
                    file.save()
                    context['done'] = True
            else:
                context['size'] = 0
        return JsonResponse(context, status=200)
