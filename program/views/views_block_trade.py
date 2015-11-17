# -*- coding: utf-8 -*-

from bson.objectid import ObjectId
from django.shortcuts import render_to_response, redirect
from django.views.generic import View, ListView
from django.template import RequestContext
from django.core.paginator import Paginator

from program.forms import BlockTradeForm
from program.models import BaseBlockTrade
from eggs.utils.form import EmptyForm


class Program(View):
    route = 'margin_trade/'

    def get(self, request):
        return redirect(self.route)


class BlockTrade(ListView):
    objects_per = 10
    objects_limit = 100
    template_name = 'margin_trade.html'

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
        form.pop('csrfmiddlewaretoken')
        pk = ObjectId(form.pop('id')[0])

        if form:
            BaseBlockTrade(pk=pk).update(**dict([(k, v) for k, v in form.items()]))
        return self.get(request)

    def delete(self, request):
        print request.POST


class MarginTrade(ListView):
    pass


class ExecutiveRegulation(ListView):
    pass


class AStockReport(ListView):
    pass


class HKStockReport(ListView):
    pass


class HKStockEquity(ListView):
    pass


class HKStockAnnouncement(ListView):
    pass
