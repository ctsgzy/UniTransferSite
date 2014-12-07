# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
import json
from django.contrib import auth
from mypacks.views import showmypacks

def showLoginPage(request):
    return render_to_response('templates/login.html', context_instance=RequestContext(request))

def loginView(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request,user)
        return HttpResponseRedirect("/mypacks/")
    else:
        return HttpResponseRedirect("/error/")

def logoutView(request):
    auth.logout(request)
    return HttpResponseRedirect("/showloginpage/")
