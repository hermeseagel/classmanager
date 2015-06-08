# coding=UTF-8
from django.db import models
from django.utils import timezone

# Create your models here.
class cls_loc(models.Model):
     loc_name = models.CharField(u'上課地點',max_length=80)

class classes(models.Model):
    class_name = models.CharField(u'課程名稱',max_length=70)
    class_id = models.BigIntegerField(u'課程代碼(純數字5碼):', max_length=100)
    class_loc = models.CharField(u'開課位置', max_length=200)
    def __unicode__(self):
        return self.class_id,self.class_name,self.class_loc
class classroom(models.Model):
    clsroom_location= models.CharField(u'教室地址', max_length=200)
    clsroom_seats =  models.CharField(u'教室座位數', max_length=200)
class Studentlist(models.Model):
    name = models.CharField(u'學生名字', max_length=100)
    mobile = models.CharField(u'mobile', max_length=15)
    prepay = models.IntegerField(u'prepay',max_length=20)
    resetfee = models.IntegerField(u'resetfree',max_length=100)
    clsid = models.ForeignKey(u'Classes')
    def __unicode__(self):
        return self.name,self.mobile,self.resetfee,self.clsid,self.prepay
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title