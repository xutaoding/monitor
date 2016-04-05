from django.template import RequestContext
from django.shortcuts import render_to_response
# from django.contrib.auth.models import User
from mongoengine.django.auth import User
from django.contrib.auth import authenticate


def login(request):
    template_name = 'login.html'

    return render_to_response(
        template_name=template_name,
        context_instance=RequestContext(request)
    )
