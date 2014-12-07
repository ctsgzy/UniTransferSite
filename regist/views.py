# -*- coding: utf-8 -*-
# Create your views here.
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.template import RequestContext
import datetime, time
from django.contrib import auth
from django.contrib.auth.models import User

def registView(request):
	errors = []
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password1 = request.POST.get('password1', '')
		usercount = User.objects.filter(username=username).count()
		if usercount > 0:
			errors = 'user exist'
			print errors
			return render_to_response('templates/regist.html',context_instance=RequestContext(request))
		else:
			user = User.objects.create_user(username, username, password1)
			user = auth.authenticate(username=username, password=password1)
			auth.login(request, user)
			return render_to_response('templates/myPacks.html', {'user': user}, context_instance=RequestContext(request))
	return render_to_response('templates/regist.html',context_instance=RequestContext(request))


