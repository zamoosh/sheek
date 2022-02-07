from .imports import *

@login_required
def jobs_api(request, parent=None):
    context = []
    if request.is_ajax and request.method == "GET":
        jobid = request.GET.get('jobid')
        job_field_id = Tag.objects.values('jobfield').filter(id=jobid)
        job_field = JobField.objects.filter(id__in=job_field_id)
        for i in job_field:
            context.append({'id': i.pk, 'title': i.title})
    return JsonResponse(context, safe=False)