from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
import json, datetime
from django.db.models import Q
from order_management.models import EDIT_PRICE_REQUEST, SUP_STEP
from django.http import JsonResponse
from order_management.models import PAYABLES
from order_management.models import RECEIVEABLES
from order_management.models import ORDER
@login_required
@permission_required('order_management.handle_edit_price_request', login_url='/error?info=没有查看改价请求的权限，请联系管理员')
def edit_price_request(request):

    if request.method == "GET":
        info = request.GET.get('info', '')
        return render(request, 'manage/edit_request.html', {'info':info})
    elif request.method == "POST":
        bo_data = json.loads(request.body.decode())

        limit      = bo_data["limit"]
        offset     = bo_data["offset"]


        data = EDIT_PRICE_REQUEST.objects.filter().values()[offset:offset+limit]
        total = EDIT_PRICE_REQUEST.objects.filter().count()
        rows = []
        index = 1
        for line in data:
            if line["type"] == "recv" or line["type"]=="recv_delete":
                recv_obj =RECEIVEABLES.objects.filter(id=line["target_id"]).first()
                if recv_obj!=None: #已删除
                    line["description"] = recv_obj.description
                    line["order_No"] = ORDER.objects.get(id=recv_obj.order_id).No
                    line["target_create_time"] = datetime.datetime.strftime((recv_obj.create_time), '%Y-%m-%d %H:%M:%S')
                    line["old_price"] = recv_obj.receiveables
            if line["type"] == "paya" or line["type"]=="paya_delete":
                paya_obj =PAYABLES.objects.filter(id=line["target_id"]).first()
                if paya_obj!=None: #已删除
                    line["description"] = paya_obj.description
                    line["order_No"] = ORDER.objects.get(id=paya_obj.order_id).No
                    line["target_create_time"] = datetime.datetime.strftime((paya_obj.create_time), '%Y-%m-%d %H:%M:%S')
                    line["old_price"] = paya_obj.payables
            if line["type"] =="recv_add":
                order_obj = ORDER.objects.filter(id=line["target_id"]).first()
                line["order_No"] = order_obj.No
                #get step list
                step_objs = SUP_STEP.objects.all()
                step_dic = {}
                for sub_line in step_objs:
                    step_dic[sub_line.id] = sub_line.name
                step_name = step_dic[line["add_step"]]
                line["description"] = step_name+"-"+line["add_desc"]
            if line["type"] =="paya_add":
                order_obj = ORDER.objects.filter(id=line["target_id"]).first()
                line["order_No"] = order_obj.No
                #get step list
                step_objs = SUP_STEP.objects.all()
                step_dic = {}
                for sub_line in step_objs:
                    step_dic[sub_line.id] = sub_line.name
                step_name = step_dic[line["add_step"]]
                line["description"] = step_name+"-"+line["add_desc"]
            line["time"] = datetime.datetime.strftime((line["time"]), '%Y-%m-%d %H:%M:%S')
            line["index"] = index
            index += 1
            rows.append(line)
        return JsonResponse({"rows":rows, "total":total})