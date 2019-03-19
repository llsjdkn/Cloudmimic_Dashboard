from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views,mtd,mimic

urlpatterns =[
    url(r'^hello$', views.index1,name='index1'),
    url(r'^mtdlist$', mtd.mtd_list, name='mtdlist'),
    url(r'^mtdlistrefresh$', mtd.mtd_list_refresh, name='mtdlistrefresh'),
    url(r'^mtd/(\w+)/$', mtd.mtd_info, name='mtd'),
    url(r'^mtdrefresh/(\w+)/$', mtd.mtd_info_refresh, name='mtdrefresh'),
    url(r'^mimiclist$', mimic.mimic_list, name='mimiclist'),
    url(r'^mimiclistrefresh$', mimic.mimic_list_refresh, name='mimiclistrefresh'),
    url(r'^mimic/(\w+)/$', mimic.mimic_info, name='mimic'),
    url(r'^mimicrefresh/(\w+)/$', mimic.mimic_info_refresh, name='mimicrefresh'),
    #url(r'^favicon.ico',RedirectView.as_view(url=r'/static/favicon.ico')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)