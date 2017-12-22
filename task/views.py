# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import QuerySet
from django.shortcuts import render
from task import models as taskModels
from shared.serializers.base import Serializer
import json
from shared.serializers.serialize_json import model_to_dict
# Create your views here.

def serialize(data, excluded='password'):
    return Serializer().serialize(data, excluded=excluded)

def task(req):
    oss = taskModels.Config.objects.raw('select id,os from config GROUP by os')
    kernels = taskModels.Config.objects.raw('select id,kernel from config GROUP by kernel')
    cpus = taskModels.Cpu.objects.raw('select id,version from cpu GROUP  by version')
    
    #TODO 这是模拟数据
    # cpu_list=[{'id':1,'text':'Hi1612'},{'id':2,'text':'Hi1616'},{'id':3,'text':'Hi1620'},{'id':4,'text':'E5-2695'},{'id':5,'text':'E5-2697A'}]
    # os_list =[{'id':1,'text':'CentOS'},{'id':2,'text':'Ubuntu'},{'id':3,'text':'Suse'},{'id':4,'text':'Redhat'}]
    # kernel_list=[{'id':1,'text':'4.7'},{'id':2,'text':'4.8'},{'id':3,'text':'4.9'}]
    os_list=[]
    cpu_list=[]
    kernel_list=[]
    for osObj in oss:
        os = {
            "id":osObj.id,
            "text":osObj.os
        }
        os_list.append(os)
    for kernelObj in kernels:
        kernel = {
            "id": kernelObj.id,
            "text": kernelObj.kernel
        }
        kernel_list.append(kernel)
    for cpuObj in cpus:
        cpu = {
            "id": cpuObj.id,
            "text": cpuObj.version
        }
        cpu_list.append(cpu)

    taskModels.Task.objects.filter()
    
    
    data = {
        'cpu':json.dumps(cpu_list),
        'os':json.dumps(os_list),
        'kernel':json.dumps(kernel_list)
    }
    return render(req,"task.html",data)