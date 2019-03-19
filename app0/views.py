from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index1(request):
  ans={}
  ans['head']='hello world'
  return render(request,'firstpage.html',ans) # 输出字典