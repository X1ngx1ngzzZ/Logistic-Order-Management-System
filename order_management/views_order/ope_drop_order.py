from django.shortcuts import redirect
import json,time, datetime
from order_management.models import ORDER
from order_management.models import PAYABLES, RECEIVEABLES, LOG_TRACE
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required


@login_required
def ope_drop_order(request):
    if not request.user.has_perm("order_management.delete_order"):
        if_success = 0
        info = "操作失败：没有删除订单的权限，请联系管理员"
        return JsonResponse({'if_success': if_success, 'info': info})
    if request.method=="POST":
        No = request.POST.get("No","")
        #联系删除这个ORDER所对应的所有应收应付款以及物流信息
        #检查只有第一状态的订单可以删除
        order_obj = ORDER.objects.filter(No=No).first()
        if order_obj==None:
            if_success = 0
            info = "订单信息不存在"
        else:#2018 6 19日修改为只要没有已收已付就可以删除（原本为只有未发货可以删除）
            recv_count = RECEIVEABLES.objects.filter(order_id=order_obj.id).count()
            paya_count = PAYABLES.objects.filter(order_id=order_obj.id).count()
            if recv_count !=0 or paya_count!=0:
                if_success=0
                info = "删除订单需要提前清空收付款信息"
            else:
                order_id = order_obj.id
                LOG_TRACE.objects.filter(order_id=order_id).delete()
                order_obj.if_delete=1
                order_obj.save()
                if_success = 1
                info = "删除成功"

        return JsonResponse({'if_success':if_success, 'info': info})

