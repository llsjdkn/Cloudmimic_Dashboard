from app0.models import MimicHistory
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import json
from datetime import datetime


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def mimic_list(request):
    return render(request,
                  'mimic_list.html')

def mimic_list_refresh(request):
    queryset = MimicHistory.objects.all()
    data = []
    for row in queryset:
        data.append(
            {'P_extern': row.p_extern,
             'E1_loca': row.e1_location, 'E1': row.e1,
             'E2_loca': row.e2_location, 'E2': row.e2,
             'E3_loca': row.e3_location, 'E3': row.e3
            # 'HappenTime': row.happentime
	     })  # 后续对接数据库修改
    print(data)
    json_data = json.dumps(data,cls = ComplexEncoder)    #json格式加双引号
    #print(json_data)mtd_list_error.html
    return JsonResponse(json_data,safe=False)


def mimic_info(request,mimicname):
    context = {}
    context['name'] = mimicname
    return render(request,
                  'mimic.html',context)


def mimic_info_refresh(request,mimicname):
    print(mimicname)
    queryset = MimicHistory.objects.filter(p_extern=mimicname).order_by('-happentime').last()
    data = []
    for row in queryset:
        data.append(
            {'P_extern': row.p_extern,
             'E1_loca': row.e1_loca, 'E1_ip': row.e1,
             'E2_loca': row.e1_loca, 'E2_ip': row.e1,
             'E3_loca': row.e1_loca, 'E3_ip': row.e1
             #'HappenTime': row.happentime
	     })
    json_data = json.dumps(data,cls = ComplexEncoder)
    print(json_data)
    return JsonResponse(json_data, safe=False)

