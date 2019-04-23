from app0.models import MtdHistory
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


def mtd_list(request):
    return render(request, 'mtd_list_error.html')


def mtd_list_refresh(request):
    queryset = MtdHistory.objects.all()
    data = []
    for row in queryset:
        data.append(
            {
            'P_extern': row.p_extern,
            'E1_loca': row.e1_location,
    'E1': row.e1,
    'HappenTime': row.happentime
    })  # 后续对接数据库修改

    print(data)
    json_data = json.dumps(data, cls=ComplexEncoder)    # json格式加双引号
    # print(json_data)
    return JsonResponse(json_data, safe=False)


def mtd_info(request, mtdname):
    context = {}
    context['name'] = mtdname
    # print(mtdname)
    return render(request, 'mtd.html', context)


def mtd_info_refresh(request, mtdname):
    # print(mtdname)
    queryset = MtdHistory.objects.filter(p_extern=mtdname).order_by('-happentime')[0, 3]  # 时间倒序排序并取前三个值
    data = []
    for row in queryset:
        data.append(
            {'P_extern': row.p_extern, 'E1_loca': row.e1_location, 'E1': row.e1,'HappenTime': row.happentime})
    print(data)    
    json_data = json.dumps(data, cls=ComplexEncoder)
    print(json_data)
    return JsonResponse(json_data, safe=False)
