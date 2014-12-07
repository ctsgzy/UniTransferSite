# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage

def defaultpage(request):
		return render_to_response('templates/login.html', context_instance=RequestContext(request))

def bootstrap_template(request):
		return render_to_response('templates/bootstrap_template.html', context_instance=RequestContext(request))