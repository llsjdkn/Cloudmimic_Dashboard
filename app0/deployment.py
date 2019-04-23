# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

# 引入我们创建的表单类
from app0.forms import AddForm


def deploy(request):
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
