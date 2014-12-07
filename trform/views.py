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
	print 'showmypacks'
	packet = Packet.objects.filter(user=request.user).order_by('-id')

	order_status_num = []
	nTotal = packet.count()
	nStatus_1 = nTotal
	nStatus_2 = 0

	packets = []

	for p in packet:
		packets.append(p)

	jd = makePacketJson(packets)

	#now just send nTotal,order,packet   need modify!!!!!!!!!!
	return render_to_response('templates/mypacks.html',{'nTotal':nTotal,'ptdata':jd},context_instance=RequestContext(request))

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
			packet = Packet(user = user,status='待入库',rep_no='',userdesc='',mgrdesc='',deliver = deliver , deliver_no = deliverno, shopping_site = shopping_site, content = t, createtime =now ,updatetime=now)
			packet.save()
	return showmypacks(request)

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
		'userdesc':p.userdesc,
		'mgrdesc':p.mgrdesc,
		'createtime':str(p.createtime),
		'updatetime':str(p.updatetime)
		}
		pdl.append(data)
	pj = json.dumps(pdl)
	return pj
