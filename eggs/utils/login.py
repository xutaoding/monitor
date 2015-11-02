from django.views.generic import View
from django.template import RequestContext
from django.shortcuts import render_to_response


class Login(View):
    def get(self, request):
        template_name = 'login.html'
        return render_to_response(template_name, context_instance=RequestContext(request))

