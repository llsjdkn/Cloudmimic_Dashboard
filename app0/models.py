from django.db import models



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












