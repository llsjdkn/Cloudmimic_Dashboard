
from django import forms


class AddForm(forms.Form):
    os = forms.CharField(max_length=100, label='类型')
    username = forms.CharField(max_length=100, label='username')
    location = forms.CharField(max_length=100, label='部署位置')
    number = forms.IntegerField(label='数量')
