# coding=utf-8

from django.db import models
from django.contrib.auth.models import AbstractUser
# create tables


class MtdHistory(models.Model):
    happentime = models.DateTimeField(db_column='HappenTime', primary_key=True)  # Field name made lowercase.
    p_extern = models.CharField(db_column='P_extern', max_length=16, blank=True, null=True)
    p_inter = models.CharField(db_column='P_inter', max_length=16, blank=True, null=True)   # Field name made lowercase.
    e1 = models.CharField(db_column='E1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    e2 = models.CharField(db_column='E2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_location = models.CharField(db_column='P_location', max_length=45, blank=True, null=True)
    e1_location = models.CharField(db_column='E1_location', max_length=45, blank=True, null=True)
    e2_location = models.CharField(db_column='E2_location', max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MTD_HISTORY'


class MimicHistory(models.Model):
    happentime = models.DateTimeField(db_column='HappenTime', primary_key=True)  # Field name made lowercase.
    p_extern = models.CharField(db_column='P_extern', max_length=16, blank=True, null=True)
    p_inter = models.CharField(db_column='P_inter', max_length=16, blank=True, null=True)  # Field name made lowercase.
    e1 = models.CharField(db_column='E1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    e2 = models.CharField(db_column='E2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    e3 = models.CharField(db_column='E3', max_length=16, blank=True, null=True)  # Field name made lowercase.
    e4 = models.CharField(db_column='E4', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_location = models.CharField(db_column='P_location', max_length=45, blank=True, null=True)
    e2_location = models.CharField(db_column='E2_location', max_length=45, blank=True, null=True)
    e3_location = models.CharField(db_column='E3_location', max_length=45, blank=True, null=True)
    e4_location = models.CharField(db_column='E4_location', max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MIMIC_HISTORY'

# add in 2019.04.19


class Userinfo(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    # username = models.CharField(verbose_name='username', max_length=32,unique=True)
    # password = models.CharField(verbose_name='userpass', max_length=64)
    description = models.TextField(max_length=64, blank=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        # ordering = ('username',)


class Sliceinfo(models.Model):
    slicename = models.CharField(verbose_name='slicename', max_length=32, unique=True)
    netname = models.CharField(verbose_name='vxlannetname', max_length=32, unique=True)
    netid = models.IntegerField(verbose_name='vxlannetid', unique=True)

    class Meta:
        verbose_name = 'qiepian'
        verbose_name_plural = verbose_name
        ordering = ('slicename',)


class Vmallocation(models.Model):
    service_type_choices = (
        ('web', 'web服务'),
        ('vnf1', 'vnf1服务'),
        ('vnf2', 'vnf2服务'),
    )
    servicelevel_type_choices = (
        (1, '购买了安全等级为1的服务'),
        (2, '购买了安全等级为2的服务'),
        (3, '购买了安全等级为3的服务'),
    )
    status_choices = (
        ('continuing', '正在提供服务功能动态轮换应用服务'),
        ('stopped', '服务已停止'),
    )

    service_type = models.CharField(max_length=32, choices=service_type_choices)
    service_level = models.IntegerField(choices=servicelevel_type_choices, null=False, default=1)  # 安全级别

    user = models.ForeignKey(Userinfo, blank=True, null=True, on_delete=models.SET_NULL)
    password = models.CharField(verbose_name='mima', max_length=32, null=False)
    slice = models.ForeignKey(Sliceinfo, blank=True, null=True, on_delete=models.SET_NULL)

    vmname = models.CharField(verbose_name='虚拟机名称', max_length=32, null=False)
    imagename = models.CharField(verbose_name='镜像名', max_length=32, null=False, default=365)  # 镜像名称
    num = models.IntegerField(verbose_name='部署数量', null=False, default=1)
    flavor = models.CharField(verbose_name='规格', max_length=32, null=False)  # 规格Flavor

    # intranet_ip = models.GenericIPAddressField(max_length=64, unique=True, null=True)  # 内网IP
    extranet_ip = models.GenericIPAddressField(max_length=64, unique=True, null=True)  # 外网IP
    zone = models.CharField(verbose_name='可用区域', max_length=32, null=True)
    service_available_time = models.IntegerField(verbose_name='购买的服务时间', null=False, default=365)  # 用户要求的服务提供 分钟 或小时

    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    taskinfo = models.TextField(null=True)
    taskstatus = models.CharField(max_length=32, choices=status_choices, null=True)

    class Meta:
        verbose_name = '动态部署任务'
        verbose_name_plural = verbose_name
        ordering = ('created',)


class Vmmigration(models.Model):
    user = models.ForeignKey(Userinfo, blank=True, null=True, on_delete=models.SET_NULL)
    password = models.CharField(verbose_name='mima', max_length=32, null=False)
    migrationvm_name = models.ForeignKey(Vmallocation, null=False, on_delete=models.CASCADE)
    serverzone_dst = models.CharField(max_length=32, null=False)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '动态迁移任务'
        verbose_name_plural = verbose_name
        ordering = ('created',)


class Mimicintecontrol(models.Model):
    service_type_choices = (
        ('web', 'web服务'),
        ('vnf1', 'vnf1服务'),
        ('vnf2', 'vnf2服务'),
    )
    servicelevel_type_choices = (
        (1, '购买了安全等级为1的服务'),
        (2, '购买了安全等级为2的服务'),
        (3, '购买了安全等级为3的服务'),
    )
    status_choices = (
        ('continuing', '正在提供服务功能动态轮换应用服务'),
        ('stopped', '服务已停止'),
    )
    arbitrule_type_choices = (
        ('23', '2/3'),
        ('24', '2/4'),
        ('34', '3/4'),
        ('35', '3/5'),
        ('45', '4/5'),
    )

    service_type = models.CharField(max_length=32, choices=service_type_choices)
    service_level = models.IntegerField(choices=servicelevel_type_choices, null=False, default=1)  # 安全级别

    user = models.ForeignKey(Userinfo, blank=True, null=True, on_delete=models.SET_NULL)
    password = models.CharField(verbose_name='mima', max_length=32, null=False)
    slice = models.ForeignKey(Sliceinfo, blank=True, null=True, on_delete=models.SET_NULL)

    arbitrule = models.IntegerField(verbose_name='裁决规则', choices=arbitrule_type_choices)
    testname = models.CharField(verbose_name='实例名称', max_length=32, unique=True, null=True)  # 实例名称
    imagename = models.CharField(verbose_name='镜像名', max_length=32, null=False, default=365)  # 镜像名称
    flavor = models.CharField(verbose_name='规格', max_length=32, null=False, default=365)  # 规格Flavor

    extranet_ip = models.GenericIPAddressField(max_length=64, unique=True, null=True)  # 外网IP

    service_available_time = models.IntegerField(verbose_name='购买的服务时间', null=False, default=365)  # 用户要求的服务提供 分钟 或小时

    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    taskinfo = models.TextField(null=True)
    taskstatus = models.CharField(max_length=32, choices=status_choices, null=True)  # bool
    intranet_ip1 = models.GenericIPAddressField(max_length=64, unique=True, null=True)  # 内网IP
    intranet_ip2 = models.GenericIPAddressField(max_length=64, unique=True, null=True)  # 内网IP
    intranet_ip3 = models.GenericIPAddressField(max_length=64, unique=True, null=True)  # 内网IP
    intranet_ip4 = models.GenericIPAddressField(max_length=64, unique=True, null=True)  # 内网IP
    intranet_ip5 = models.GenericIPAddressField(max_length=64, unique=True, null=True)  # 内网IP

    class Meta:
        verbose_name = '拟态封装任务'
        verbose_name_plural = verbose_name
        ordering = ('created',)

# class manage(models.Model):
#     username = models.CharField(verbose_name='用户名', max_length=32, null=False)#输入用户名，查询数据库返回其任务信息
#
#     class Meta:
#         verbose_name = '管理参数任务'
#         verbose_name_plural = verbose_name
#         #ordering = ('created',)


class Mimicimage(models.Model):
    service_type_choices = (
        ('web', 'web服务'),
        ('vnf1', 'vnf1服务'),
        ('vnf2', 'vnf2服务'),
    )
    imagename = models.CharField(verbose_name='镜像名', max_length=32, null=False, default=365)  # 镜像名称
    service_type = models.CharField(max_length=32, choices=service_type_choices)
    appversion = models.IntegerField(null=True, default=1)
    osname = models.CharField(verbose_name='镜像操作系统', max_length=32, null=False)
    filepath = models.CharField(verbose_name='镜像路径', max_length=32, null=False)
    created = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    #  imagefile=    本地文件上传

    class Meta:
        verbose_name = '接口传入参数任务'
        verbose_name_plural = verbose_name
        ordering = ('created',)

