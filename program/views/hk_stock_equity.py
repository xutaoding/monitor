from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render_to_response


class HKStockEquityView(View):
    template_name = 'hk_stock_equity.html'

    def get(self, request):
        return render_to_response(self.template_name)

    def post(self, request):
        return HttpResponse('{"msg": 1}')
