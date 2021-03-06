from django.http import JsonResponse
from order_management.models import LOG_TRACE
import json,time, datetime
from django.contrib.auth.decorators import login_required


@login_required
def get_trace_data(request):
    if not request.user.has_perm("order_management.view_order"):
        return JsonResponse({'rows': []})
    id = request.POST.get("id")
    objs = LOG_TRACE.objects.filter(order_id=id)
    rows = []
    for line in objs:
        rows.append({
            "trace_id":line.id,
            "status": line.status,
            "create_time": datetime.datetime.strftime(line.create_time, '%Y-%m-%d %H:%M:%S'),
            "select_time": datetime.datetime.strftime(line.select_time, '%m/%d/%Y'),
            "desc": line.desc,
            "create_user": line.create_user,
        })
    return JsonResponse({
        "rows": rows,
    })