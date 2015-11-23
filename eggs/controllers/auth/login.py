from django.views.generic import View
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate

from .models import User


class Login(View):
    def get(self, request):
        print type(User)
        template_name = 'login.html'
        return render_to_response(template_name, context_instance=RequestContext(request))

