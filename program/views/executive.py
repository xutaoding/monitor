from django.views.generic import View
from django.shortcuts import render_to_response


class ExecutiveRegulationView(View):
    template_name = '404.html'

    def get(self, request):
        return render_to_response(self.template_name)
