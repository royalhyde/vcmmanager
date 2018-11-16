from django.http import HttpResponse
import json
from django.shortcuts import render
from worker.models import vcms
from worker.models import servers
from worker.models import records2dict


def index(request):
    global context
    context = {}
    return render(request, 'worker/index.html')


def listvcm(request):
    context = {}
    vcmlist = vcms.objects.all()
    outdict = records2dict(vcmlist, 'vcm')
    outstr = json.dumps(outdict)
    return HttpResponse(outstr, content_type="application/json")


# context['vcmlist'] = vcmlist
# return render(request, 'worker/listvcm.html', context)
# return render(request, 'worker/listvcm.html')


def listserver(request):
    context = {}
    serverlist = servers.objects.all()
    outdict = records2dict(serverlist, 'server')
    outstr = json.dumps(outdict)
    return HttpResponse(outstr, content_type="application/json")


# context['serverlist'] = serverlist
# return render(request, 'worker/listserver.html', context)
# return render(request, 'worker/listserver.html')


def applyvcm(request):
    context = {}
    vcmidle = vcms.objects.filter(busy='idle')
    if vcmidle.count() > 0:
        context['getvcm'] = vcmidle[0].name
        row = vcmidle[0]
        row.busy = 'busy'
        row.save()
    return render(request, 'worker/applyvcm.html', context)


def delvcm(request):
    context = {}
    vcmbusy = vcms.objects.filter(busy='busy')
    if vcmbusy.count() > 0:
        context['getvcm'] = vcmbusy[0].name
        row = vcmbusy[0]
        row.busy = 'idle'
        row.save()
    return render(request, 'worker/delvcm.html', context)


# return render(request, 'worker/delvcm.html')


def regserver(request):
    context = {}
    return render(request, 'worker/regserver.html', context)
    # return render(request, 'worker/regserver.html')
