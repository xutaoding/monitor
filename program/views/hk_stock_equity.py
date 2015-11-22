# -*- coding: utf-8 -*-

import re
import json
from django.views.generic import View
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect


class HKStockEquityView(View):
    template_name = 'hk_stock_equity.html'

    def get(self, request):
        return render_to_response(
            template_name=self.template_name,
            context_instance=RequestContext(request)
        )


class StockEquityCodeView(View):
    config_path = 'E:/temp/stock_equity.txt'
    run_command = 'python xxx/stock_equity.py {}'

    @property
    def total_codes(self):
        total_hk_codes = set()

        with open(self.config_path) as fp:
            for line in fp:
                if line.strip():
                    total_hk_codes.add(line.strip())
        return total_hk_codes

    def get(self, request):
        code = request.GET.get('code', '').strip()

        if not code:
            return HttpResponse(json.dumps({'msg': None}))

        if code in self.total_codes:
            msg = {'code': code, 'msg': u'该代码在配置文件中'}
        else:
            msg = {'code': code, 'msg': u'该代码不在配置文件中，请添加该代码'}
        return HttpResponse(json.dumps(msg))

    def post(self, request):
        code = request.POST.get('code', '')

        if len(code) != 5:
            return HttpResponse(json.dumps({'code': code, 'msg': u'代码输入有误，不是5位数字'}))

        total_codes = self.total_codes
        total_codes.add(code)

        with open(self.config_path, 'w') as fp:
            fp.writelines('\n'.join(sorted(total_codes)))
        return HttpResponse(json.dumps({'code': code, 'msg': u'该代码添加成功'}))

    def put(self, request):
        m_code = re.compile(r'\d{5}').search(request.read())

        if m_code is None:
            return HttpResponse(json.dumps({'code': m_code.group(), 'msg': u'代码输入有误'}))

        # run command script
        pass




