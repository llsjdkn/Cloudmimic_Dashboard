# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Mimic(models.Model):
    p_flip = models.CharField(db_column='P_flip', primary_key=True, max_length=16)  # Field name made lowercase.
    p_fix = models.CharField(db_column='P_fix', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_id = models.CharField(db_column='P_id', max_length=45, blank=True, null=True)  # Field name made lowercase.
    e1_fix = models.CharField(max_length=45, blank=True, null=True)
    e1_id = models.CharField(max_length=45, blank=True, null=True)
    e2_fix = models.CharField(max_length=45, blank=True, null=True)
    e2_id = models.CharField(max_length=45, blank=True, null=True)
    e3_fix = models.CharField(max_length=45, blank=True, null=True)
    e3_id = models.CharField(max_length=45, blank=True, null=True)
    e4_fix = models.CharField(max_length=45, blank=True, null=True)
    e4_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MIMIC'


class MimicHistory(models.Model):
    happentime = models.DateTimeField(db_column='HappenTime', primary_key=True)  # Field name made lowercase.
    p_extern = models.CharField(db_column='P_extern', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_inter = models.CharField(db_column='P_inter', max_length=16, blank=True, null=True)  # Field name made lowercase.
    e1 = models.CharField(db_column='E1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    e2 = models.CharField(db_column='E2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    e3 = models.CharField(db_column='E3', max_length=16, blank=True, null=True)  # Field name made lowercase.
    e4 = models.CharField(db_column='E4', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_location = models.CharField(db_column='P_location', max_length=45, blank=True, null=True)  # Field name made lowercase.
    e1_location = models.CharField(db_column='E1_location', max_length=45, blank=True, null=True)  # Field name made lowercase.
    e2_location = models.CharField(db_column='E2_location', max_length=45, blank=True, null=True)  # Field name made lowercase.
    e3_location = models.CharField(db_column='E3_location', max_length=45, blank=True, null=True)  # Field name made lowercase.
    e4_location = models.CharField(db_column='E4_location', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MIMIC_HISTORY'


class Mtd(models.Model):
    p_flip = models.CharField(db_column='P_flip', primary_key=True, max_length=16)  # Field name made lowercase.
    p_fix = models.CharField(db_column='P_fix', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_id = models.CharField(db_column='P_id', max_length=255, blank=True, null=True)  # Field name made lowercase.
    e1_fix = models.CharField(max_length=16, blank=True, null=True)
    e1_id = models.CharField(max_length=255, blank=True, null=True)
    e2_fix = models.CharField(max_length=16, blank=True, null=True)
    e2_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MTD'


class MtdHistory(models.Model):
    happentime = models.DateTimeField(db_column='HappenTime', primary_key=True)  # Field name made lowercase.
    p_extern = models.CharField(db_column='P_extern', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_inter = models.CharField(db_column='P_inter', max_length=16, blank=True, null=True)  # Field name made lowercase.
    e1 = models.CharField(db_column='E1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    e2 = models.CharField(db_column='E2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_location = models.CharField(db_column='P_location', max_length=45, blank=True, null=True)  # Field name made lowercase.
    e1_location = models.CharField(db_column='E1_location', max_length=45, blank=True, null=True)  # Field name made lowercase.
    e2_location = models.CharField(db_column='E2_location', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MTD_HISTORY'


class ApiServicecat(models.Model):
    service_type = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'api_servicecat'


class ApiTaskdynamic(models.Model):
    username = models.CharField(max_length=32)
    mima = models.CharField(max_length=64)
    taskname = models.CharField(unique=True, max_length=64, blank=True, null=True)
    fip = models.CharField(db_column='Fip', unique=True, max_length=39, blank=True, null=True)  # Field name made lowercase.
    service_available_time = models.IntegerField()
    created = models.DateTimeField()
    taskinfo = models.TextField(blank=True, null=True)
    flavor = models.CharField(max_length=32)
    imagename = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'api_taskdynamic'


class ApiTaskmimic(models.Model):
    service_type = models.CharField(max_length=32)
    service_level = models.IntegerField()
    username = models.CharField(max_length=32)
    mima = models.CharField(max_length=64)
    taskname = models.CharField(unique=True, max_length=64, blank=True, null=True)
    fip = models.CharField(db_column='Fip', unique=True, max_length=39, blank=True, null=True)  # Field name made lowercase.
    service_available_time = models.IntegerField()
    created = models.DateTimeField()
    taskinfo = models.TextField(blank=True, null=True)
    taskstatus = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_taskmimic'


class ApiTaskmtd(models.Model):
    service_type = models.CharField(max_length=32)
    service_level = models.IntegerField()
    username = models.CharField(max_length=32)
    mima = models.CharField(max_length=64)
    taskname = models.CharField(unique=True, max_length=64, blank=True, null=True)
    fip = models.CharField(db_column='Fip', unique=True, max_length=39, blank=True, null=True)  # Field name made lowercase.
    service_available_time = models.IntegerField()
    created = models.DateTimeField()
    taskinfo = models.TextField(blank=True, null=True)
    taskstatus = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_taskmtd'


class ApiUserinfo(models.Model):
    username = models.CharField(unique=True, max_length=32)
    mima = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'api_userinfo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
