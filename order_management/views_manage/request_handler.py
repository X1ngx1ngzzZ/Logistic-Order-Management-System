from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
import json, datetime
from django.db.models import Q
from order_management.models import EDIT_PRICE_REQUEST
from django.http import JsonResponse
from order_management.models import PAYABLES
from order_management.models import RECEIVEABLES
from order_management.models import ORDER
@login_required
@permission_required('order_management.handle_edit_price_request', login_url='/error?info=没有查看改价请求的权限，请联系管理员')
def request_handler(request):
    if request.method == "POST":
        request_id = request.POST.get("id")
        if_accept  = request.POST.get("if_accept")  #如果是0代表拒绝，如果是1代表接受
        if_success = 0
        info = ""
        if if_accept=="1":
            request_obj = EDIT_PRICE_REQUEST.objects.filter(id=request_id).first()
            if request_obj==None:
                info = "申请已经被删除"
            else:
                type = request_obj.type
                if type=="recv":
                    recv_obj = RECEIVEABLES.objects.filter(id=request_obj.target_id).first()
                    if recv_obj != None:
                        recv_obj.receiveables = request_obj.target_price
                        recv_obj.save()
                        if_success = 1
                    else:
                        info = "目标分录已经被删除"
                elif type == "paya":
                    paya_obj = PAYABLES.objects.filter(id=request_obj.target_id).first()
                    if paya_obj != None:
                        paya_obj.payables = request_obj.target_price
                        paya_obj.save()
                        if_success = 1
                    else:
                        info = "目标分录已经被删除"
                elif type == "recv_delete":
                    recv_obj = RECEIVEABLES.objects.filter(id=request_obj.target_id).first()
                    if recv_obj != None:
                        recv_obj.delete()
                        if_success = 1
                    else:
                        info = "目标分录已经被删除"
                elif type == "paya_delete":
                    paya_obj = PAYABLES.objects.filter(id=request_obj.target_id).first()
                    if paya_obj != None:
                        paya_obj.delete()
                        if_success = 1
                    else:
                        info = "目标分录已经被删除"
                elif type == "recv_add":
                    order_obj = ORDER.objects.get(id=request_obj.target_id)
                    RECEIVEABLES.objects.create(status=0, order_id=request_obj.target_id, description=request_obj.add_desc,
                                                receiveables=request_obj.target_price, received=0, step=request_obj.add_step,
                                                client_id=request_obj.add_cs_id)
                    order_obj.status=4
                    order_obj.save()
                    if_success = 1
                elif type == "paya_add":
                    order_obj = ORDER.objects.get(id=request_obj.target_id)
                    PAYABLES.objects.create(status=0, order_id=request_obj.target_id, description=request_obj.add_desc,
                                                payables=request_obj.target_price, paid_cash=0, paid_oil=0, step=request_obj.add_step,
                                                supplier_id=request_obj.add_cs_id, client_id=order_obj.client_id)
                    if_success = 1
                else:
                    if_success=0
                    info = "要求操作没有预先定义"
                if if_success==1:
                    request_obj.delete()
        elif if_accept=="0":
            request_obj = EDIT_PRICE_REQUEST.objects.filter(id=request_id).first()
            if request_obj == None:
                info = "申请已经被删除"
            else:
                request_obj.delete()
                if_success = 1
        else:
            if_success = 0
            info = "批准失败，参数错误"
        return JsonResponse({"if_success":if_success, "info":info})