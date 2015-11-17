# -*- coding: utf-8 -*-

import re
import json
from bson.objectid import ObjectId
from django.http.response import HttpResponse
from django.views.generic import ListView
from django.template import RequestContext
from django.core.paginator import Paginator
from django.shortcuts import render_to_response

from program.forms import BlockTradeForm
from program.models import BaseBlockTrade
from eggs.utils.form import EmptyForm


class BlockTradeView(ListView):
    objects_per = 10
    objects_limit = 100
    template_name = 'block_trade.html'

    @staticmethod
    def trim_query_string(queries):
        query = queries.copy()
        for key, value in query.items():
            query[key] = value.strip()
        return query

    def queryset(self, form=None):
        form = EmptyForm() if form is None else form
        query = {k: v for k, v in form.data.items() if v}

        return list(BaseBlockTrade.objects(**query).order_by('-y').limit(self.objects_limit))

    def get(self, request, *args, **kwargs):
        form = self.trim_query_string(request.GET)
        page = int(form.get('page')) if form.get('page') else 1
        form = BlockTradeForm(form)

        queryset = self.queryset(form)
        paginator = Paginator(queryset, self.objects_per)
        objects_list = paginator.page(page)

        return render_to_response(
            self.template_name,
            {'objects_list': objects_list, 'form': form},
            context_instance=RequestContext(request),
        )

    def post(self, request):
        form = request.POST.copy()
        ignore_keys = ['csrfmiddlewaretoken', 'id']
        update_data = dict([(k, v) for k, v in form.items() if k not in ignore_keys])

        if form:
            BaseBlockTrade(pk=ObjectId(form['id'])).update(**update_data)
        return self.get(request)

    def delete(self, request):
        pk_regex = re.compile(r'id=(?P<pk>.+)').search(request.read())

        if pk_regex is None:
            return HttpResponse(json.dumps({'msg': '数据请求错误!', 'success': False}))

        BaseBlockTrade(pk=ObjectId(pk_regex.groupdict()['pk'])).delete()
        return HttpResponse(json.dumps({'msg': '删除成功!',  'success': True}))

