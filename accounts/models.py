from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group

class MyUser(AbstractUser):

    '''
        This model for custom user
    '''
    passwordtxt = models.TextField(null = True , blank = True)
    id = models.IntegerField(primary_key=True)
    personal_P = models.BooleanField(default=False,null=True)
    startup_P = models.BooleanField(default=False,null=True)
    phone_number = models.CharField(max_length = 250 , null = True , blank = True , default='')
    age=models.IntegerField(null = True , blank = True,)
    skill=models.TextField(null = True , blank = True, default='')
    money=models.IntegerField( null = True , blank = True)
    address=models.CharField(max_length = 250 , null = True , blank = True, default='')
    code_meli=models.IntegerField(  null = True , blank = True)
    company_history=models.TextField(max_length=250,null=True, default='')
    description=models.TextField(max_length=250,null=True, default='')
    can_edit = models.BooleanField(default=False,null=True)
    p_access = models.BooleanField(default=False,null=True)
    see_users = models.BooleanField(default=False,null=True)
    







