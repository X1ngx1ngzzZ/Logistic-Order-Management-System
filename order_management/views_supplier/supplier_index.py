from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

@login_required
@permission_required('order_management.view_supplier', login_url='/error?info=操作失败：没有查看供应商的权限')
def supplier_index(request):

    if request.method == "GET":
        info = request.GET.get('info','')
        return render(request, 'supplier/index.html', {'info':info})