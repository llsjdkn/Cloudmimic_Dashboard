# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import requests

# 引入我们创建的表单类
from .forms import AddForm


def mimic_deploy(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            os = form.cleaned_data['os']
            location = form.cleaned_data['location']
            number = form.cleaned_data['number']
            flvaor = form.cleaned_data['flavor']
            return HttpResponse(str(os))
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'mimic.html', {'form': form})


def deploy(request):

    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            os = form.cleaned_data['os']
            location = form.cleaned_data['location']
            number = form.cleaned_data['number']
            flvaor = form.cleaned_data['flavor']
            url = "http://127.0.0.1:8000/api/tasksmtd/"

            payload = "{\"service_type\":\"mimic-web\",\"username\":\"lwy1\",\"mima\":\"123456\"}"
            headers = {
                'Content-Type': "application/json",
                'cache-control': "no-cache",
                'Postman-Token': "424cd4ae-f2f3-4a7a-9a20-4b6fd55aff8e"
            }

            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            # return response
            return HttpResponse(str(os))
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'deployment.html', {'form': form})


def develop(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            os = form.cleaned_data['os']
            location = form.cleaned_data['location']
            number = form.cleaned_data['number']
            flvaor = form.cleaned_data['flavor']
            return HttpResponse(str(os))
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'developerAPI.html', {'form': form})


def intecontrol(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            os = form.cleaned_data['os']
            location = form.cleaned_data['location']
            number = form.cleaned_data['number']
            flvaor = form.cleaned_data['flavor']
            return HttpResponse(str(os))
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'intecontrol.html', {'form': form})


def migration(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            os = form.cleaned_data['os']
            location = form.cleaned_data['location']
            number = form.cleaned_data['number']
            flvaor = form.cleaned_data['flavor']
            return HttpResponse(str(os))
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'migration.html', {'form': form})


def ex(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            os = form.cleaned_data['os']
            location = form.cleaned_data['location']
            number = form.cleaned_data['number']
            flvaor = form.cleaned_data['flavor']
            return HttpResponse(str(os))
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'mimic_exhibition.html', {'form': form})


def ex2(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            os = form.cleaned_data['os']
            location = form.cleaned_data['location']
            number = form.cleaned_data['number']
            flvaor = form.cleaned_data['flavor']
            return HttpResponse(str(os))
    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'test2.html', {'form': form})