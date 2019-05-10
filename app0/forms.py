
from django import forms


class AddForm(forms.Form):
    os = forms.CharField(max_length=100, label='类型')
    flavor = forms.CharField(max_length=100, label='参数')
    location = forms.CharField(max_length=100, label='部署位置')
    number = forms.IntegerField(label='数量')
    # migrationvm_name = forms.CharField(max_length=100, label='1')
    # serverzone_dst = forms.CharField(max_length=100, label='2')
    # filepath = forms.CharField(max_length=100, label='3')
    # imagename = forms.CharField(max_length=100, label='4')
    # service_type = forms.CharField(max_length=100, label='5')
    # appversion = forms.CharField(max_length=100, label='6')
    # osname = forms.CharField(max_length=100, label='7')

    # created = range(1, 30)
    # service_type_choices = (
    #     ('web', 'web服务'),
    #     ('vnf1', 'vnf1服务'),
    #     ('vnf2', 'vnf2服务'),
    # )
    #
    # servicelevel_type_choices = (
    #     (1, '购买了安全等级为1的服务'),
    #     (2, '购买了安全等级为2的服务'),
    #     (3, '购买了安全等级为3的服务'),
    # )
    # status_choices = (
    #     ('continuing', '正在提供服务功能动态轮换应用服务'),
    #     ('stopped', '服务已停止'),
    # )
    # arbitrule_type_choices = (
    #     ('23', '2/3'),
    #     ('24', '2/4'),
    #     ('34', '3/4'),
    #     ('35', '3/5'),
    #     ('45', '4/5'),
    # )

    # 读取数据库，这样将返回一个Queue对象，可以通过这个对象查找对应的元素，不过数据库要有一个__unicode__方法返回队列名字。
    # queue = forms.ModelChoiceField(label=u'队列', queryset= Queue.objects.all())