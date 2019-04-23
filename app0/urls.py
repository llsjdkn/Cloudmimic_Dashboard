from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views, mtd, mimic, deployment

urlpatterns = [
    url(r'^gobang$', views.index1, name='index'),     # 五子棋游戏
    url(r'^mtdlist$', mtd.mtd_list, name='mtdlist'),  # 显示mtd_list失败
    # url(r'^deployment/(\w+)/$', deployment.mtd_info, name='deployment'),  # 匹配任意字段数字
    url(r'^deployment$', deployment.deploy, name='deployment'),  # 虚拟机部署
    url(r'^migration$', deployment.migration, name='migration'),  # 虚拟机迁移
    url(r'^intecontrol$', deployment.intecontrol, name='intecontrol'),  # 智能控制功能
    url(r'^developerAPI$', deployment.develop, name='developerAPI'),  # 智能控制功能
    url(r'^mtdlistrefresh$', mtd.mtd_list_refresh, name='mtdlistrefresh'),
    url(r'^mtd/(\w+)/$', mtd.mtd_info, name='mtd'),   # 匹配任意字段数字
    url(r'^mtdrefresh/(\w+)/$', mtd.mtd_info_refresh, name='mtdrefresh'),
    url(r'^mimiclist$', mimic.mimic_list, name='mimiclist'),
    url(r'^mimiclistrefresh$', mimic.mimic_list_refresh, name='mimiclistrefresh'),
    url(r'^mimic/(\w+)/$', mimic.mimic_info, name='mimic'),
    url(r'^mimicrefresh/(\w+)/$', mimic.mimic_info_refresh, name='mimicrefresh'),
    #  url(r'^favicon.ico',RedirectView.as_view(url=r'/static/favicon.ico')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
