from django.shortcuts import render

# Create your views here.

from order_management.views_user.log_in_index import *
from order_management.views_user.log_out import *
from order_management.views_user.page_index import *
from order_management.views_user.ope_receive_bug import *

from order_management.views_client.client_index import *
from order_management.views_client.client_get_table_data import *
from order_management.views_client.client_add import *
from order_management.views_client.client_edit import *
from order_management.views_client.ope_delete_client import *
from order_management.views_client.ope_edit_client import *
from order_management.views_client.get_client_options import *
from order_management.views_client.get_client_detail import *

from order_management.views_supplier.supplier_index import *
from order_management.views_supplier.supplier_get_table_data import *
from order_management.views_supplier.supplier_add import *
from order_management.views_supplier.supplier_edit import *
from order_management.views_supplier.ope_delete_supplier import *
from order_management.views_supplier.ope_edit_supplier import *
from order_management.views_supplier.get_supplier_options import *
from order_management.views_supplier.get_sup_step_options import *

from order_management.views_order.order_index import *
from order_management.views_order.order_add import *
from order_management.views_order.order_edit import *
from order_management.views_order.ope_add_order import *
from order_management.views_order.ope_drop_order import *
from order_management.views_order.order_detail import *
from order_management.views_order.ope_add_trace import *
from order_management.views_order.get_trace_data import *
from order_management.views_order.ope_edit_trace import *
from order_management.views_order.order_price import *
from order_management.views_order.ope_trigger_close_order import *


from order_management.views_finance.finance_index import *
from order_management.views_finance.ope_paya import *
from order_management.views_finance.ope_recv import *
from order_management.views_finance.invoice_management import *

from order_management.views_manage.operate_log_index import *
from order_management.views_manage.get_order_dropped import *
from order_management.views_manage.edit_price_request import *
from order_management.views_manage.request_handler import *


from order_management.views_graph.graph_client import *
from order_management.views_graph.graph_supplier import *

from django.shortcuts import render
def error(reqeust):
    info = reqeust.GET.get("info","")
    return render(reqeust, 'error.html',{"info":info})

def page_not_found(request):
    return render(request, '404.html')