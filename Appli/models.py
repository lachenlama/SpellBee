from django.db import models

# Create your models here.

class Sheet1(models.Model):
    serialno = models.AutoField(primary_key=True)
    word = models.CharField(blank=True, null=True)
    origin = models.CharField(blank=True, null=True)
    meaning = models.CharField(blank=True, null=True)
    sentence = models.CharField(blank=True, null=True)
    used = models.BooleanField(default= False, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sheet1'


class Sheet2(models.Model):
    serialno = models.AutoField(primary_key=True)
    word = models.CharField(blank=True, null=True)
    origin = models.CharField(blank=True, null=True)
    meaning = models.CharField(blank=True, null=True)
    sentence = models.CharField(blank=True, null=True)
    used = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sheet2'


class Sheet3(models.Model):
    serialno = models.AutoField(primary_key=True)
    word = models.CharField(blank=True, null=True)
    origin = models.CharField(blank=True, null=True)
    meaning = models.CharField(blank=True, null=True)
    sentence = models.CharField(blank=True, null=True)
    used = models.BooleanField(default=False,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sheet3'


class Sheet4(models.Model):
    serialno = models.AutoField(primary_key=True)
    word = models.CharField(blank=True, null=True)
    origin = models.CharField(blank=True, null=True)
    meaning = models.CharField(blank=True, null=True)
    sentence = models.CharField(blank=True, null=True)
    used = models.BooleanField(default=False ,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sheet4'


class Sheet5(models.Model):
    serialno = models.AutoField(primary_key=True)
    word = models.CharField(blank=True, null=True)
    origin = models.CharField(blank=True, null=True)
    meaning = models.CharField(blank=True, null=True)
    sentence = models.CharField(blank=True, null=True)
    used = models.BooleanField(default=False ,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sheet5'