# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import json
from worker.models import vcms
from worker.models import servers


def index(request):
    global context
    context = {}
    return render(request, 'state/index.html')


def reportstate(request):
    context = {}
    return render(request, 'state/reportstate.html')


def doreport(request):
    outstr=''
    if request.method == 'POST':
        rawdata= request.POST['jsondata']
        reportdata= json.loads(rawdata)
        for server in reportdata:
            for vm in reportdata[server]:
                oldState = vcms.objects.filter(server=server, name=vm)
                if oldState.count() > 0 and 'busy' in reportdata[server][vm] and reportdata[server][vm]['busy'] != oldState[0].busy:
                    newState = oldState[0]
                    newState.busy = reportdata[server][vm]['busy']
                    outstr += vm
                    newState.save()
    return HttpResponse(outstr, content_type="application/json")
    #return render(request, 'state/reportstate.html',  context)

