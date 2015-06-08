#-*-coding:utf-8-*-
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
#from django.contrib.auth.decorators import login_required
from .models import classes
from .forms  import ClassForm
from django.shortcuts import render_to_response
from django.utils.cache import add_never_cache_headers
import traceback
from django.core.serializers.json import DjangoJSONEncoder
def addclass(request):
    if request=="POST":
        form =ClassForm(data = request.POST)
        if form.is_valid():
            form.save()
            sucess  = True
            sucessinfo = "增加新課程"
            return render_to_response('classstatus.html',{"title":'新增課程','form':form,'successinfo'})
        else:
            form=ClassForm()
def listclass(request):
    classlist= classes.objects.all().reverse()
    columnIndexmap={0:'cls_id',1:'class_loc'}
def classtest(request):
    return  render_to_response('classstatus.html',{"title":'課程資訊',"classid":'Tainam0001'})
