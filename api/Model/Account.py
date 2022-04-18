
from django.db import models

class Account(models.Model):
    account_id  = models.AutoField(primary_key = True)
    name        = models.CharField(max_length = 100, null = False)
    id          = models.CharField(max_length = 100, unique = True)
    email       = models.CharField(max_length = 100, unique = True)
    pwd         = models.CharField(max_length = 128, null = False)
    salt        = models.CharField(max_length = 128, null = False)
    is_login    = models.PositiveSmallIntegerField(default = 0)
    is_deleted  = models.PositiveSmallIntegerField(default = 0)
    login_dt    = models.DateTimeField(null = True)
    logout_dt   = models.DateTimeField(null = True)
    created_dt  = models.DateTimeField(auto_now_add = True)
    modified_dt = models.DateTimeField(auto_now_add = True)

    class Meta:
        managed  = False
        db_table = 'account'