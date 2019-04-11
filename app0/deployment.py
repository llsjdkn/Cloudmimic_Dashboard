# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import requests

# 引入我们创建的表单类
from app0.forms import AddForm

url = "http://127.0.0.1:8000/api/tasksmtd/"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "4b44cbb1-7cc8-41a2-82f2-ea37c3338fb6"
    }


def deploy(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            os = form.cleaned_data['os']
            location = form.cleaned_data['location']
            number = form.cleaned_data['number']
            username = form.cleaned_data['username']
            # username = 'lwy'

            payload = "{\"service_type\":\"mimic-web\",\"username\":\"lwy1\",\"mima\":\"123456\"}"
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            return HttpResponse(str(os))

    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'deployment.html', {'form': form})
