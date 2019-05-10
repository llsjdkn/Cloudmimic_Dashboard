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


def mimic_info_refresh_old(request,mimicname):
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

def mimic_info_refresh(request):
    queryset1 = MimicHistory.objects.values('p_extern') #后续数据库可以加上代理的名字，因此时代理外部ip不变可用之替代
    #print(queryset1)
    list1 = [] #list类型
    for row in queryset1:
        m=row['p_extern']
        list1.append(m)
    #print(list1)
    list2 = list(set(list1))
    #print(list2)

    nodes = [] #list类型，list元素类型为dict
    edges = []
    data = []
    for i in range(len(list2)):
        #print("list[i]:", list2[i])
        queryset2 = MimicHistory.objects.filter(p_extern=list2[i]).order_by('-happentime').last()
        #print('queryset2:', queryset2)
        #print('queryset2.p_extern:', queryset2.p_extern)
        n = len(nodes)
        nodes.append({
            'name': queryset2.p_extern,
            'image': 'http://192.168.170.198/2.png'})
        nodes.append({
            'name':  queryset2.e1,
            'image': 'http://192.168.170.198/VM.png'})
        nodes.append({
            'name':  queryset2.e2,
            'image': 'http://192.168.170.198/VM.png'})
        nodes.append({
            'name':  queryset2.e3,
            'image': 'http://192.168.170.198/VM.png'})
        edges.append({
            'source': n,
            'target': n+1,
            'relation': n})
        edges.append({
            'source': n,
            'target': n+2,
            'relation': n})
        edges.append({
            'source': n,
            'target': n+3,
            'relation': n})
    data.append({
        'nodes': nodes,
        'edges': edges})
    json_data = json.dumps(data)
    print(json_data)
    return JsonResponse(json_data, safe=False)