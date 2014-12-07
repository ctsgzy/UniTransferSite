# -*- coding: utf-8 -*-
# Create your views here.
# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.template import RequestContext
import datetime, time
import json
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from mypacks.models import Packet

@login_required
def showmypacks(request):
	user = request.user
	nTotal = getpackets(user,'0').count()
	nStatus_1 = getpackets(user,'1').count()
	nStatus_2 = getpackets(user,'2').count()	
	print(nStatus_1)
	if user.is_superuser:
		return render_to_response('templates/allpacks.html',{'nTotal':nTotal,'nStatus_1':nStatus_1,'nStatus_2':nStatus_2},context_instance=RequestContext(request))
	else:
		return render_to_response('templates/mypacks.html',{'nTotal':nTotal,'nStatus_1':nStatus_1,'nStatus_2':nStatus_2},context_instance=RequestContext(request))

def orderpackinput(request):
	return render_to_response('templates/orderpack.html',context_instance=RequestContext(request))

def orderpacksubmit(request):
	if request.method == 'POST':
		user=request.user
		deliver = request.POST.get('deliver','')
		deliverno = request.POST.get('deliver_no','')
		shopping_site = request.POST.get('shopping_site','')
		packetsnum = request.POST.get('packscount','')
		pkcontent = []
		for i in range(1 , (int(packetsnum)+1)):
			index = 'deliverContent' + str(i)
			con = request.POST.get(index,'')
			pkcontent.append(con)
		for t in pkcontent:
			now = datetime.datetime.now()
			packet = Packet(user = user,status='待入库',rep_no='',deliver = deliver , deliver_no = deliverno, shopping_site = shopping_site, content = t, createtime =now ,updatetime=now)
			packet.save()
	return showmypacks(request)

def getpacksaj(request):
	print 'getpacksaj' + '1111111111111'
	user = request.user
	status = request.GET.get('status')
	packet = getpackets(user,status)
	jd = makePacketJson(packet)
	return HttpResponse(jd)

def makePacketJson(packets):
	pdl = []
	for p in packets:
		data={
		'id':str(p.id),
		'deliver':p.deliver,
		'deliver_no':p.deliver_no,
		'shopping_site':p.shopping_site,
		'content':p.content,
		'status':p.status,
		'rep_no':p.rep_no,
		'createtime':str(p.createtime),
		'updatetime':str(p.updatetime)
		}
		pdl.append(data)
	pj = json.dumps(pdl)
	return pj

def getpackets(user,status):
	packets = {}
	if status == '1':
		if user.is_superuser:
			packets = Packet.objects.filter(status='待入库').order_by('-id')
		else:
			packets = Packet.objects.filter(user=user,status='待入库').order_by('-id')
	elif(status == '2'):
		if user.is_superuser:
			packets = Packet.objects.filter(status='已入库').order_by('-id')
		else:
			packets = Packet.objects.filter(user=user,status='已入库').order_by('-id')
	else:
		if user.is_superuser:
			packets = Packet.objects.all().order_by('-id')
		else:
			packets = Packet.objects.filter(user=user).order_by('-id')			
	return 	packets

