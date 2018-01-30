from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

@login_required
@permission_required('order_management.view_client', login_url='/no_perm/')
def client_index(request):

    if request.method == "GET":
        info = request.GET.get('info', '')
        return render(request, 'client/index.html', {'info':info})