#below is create forms from Models.
from django.forms import ModelForm
#from studentmanger.models import Post
from .forms import ClassForm
from django.shortcuts import render
from django.shortcuts import render_to_response
def classes_new(request):
    cls_form = ClassForm()
    return render(request,'ClassAdd.html',{'form': cls_form})
def classtest(request):
    return  render_to_response('classstatus.html',{"title":'課程資訊',"classid":'Tainam0001'})




#from .forms import PostForm
#from django.shortcuts import render
#def post_new(request):
#    form = PostForm()
#    return render(request, 'blogtest.html', {'form': form})





#below is old
'''from django.http import HttpResponse
from django import forms
from django.core.exceptions import ValidationError
form django.shortcuts import render_to_response
from studentmanger.models import Classes











class clsasform(forms.ModelForm):
    classname = forms.CharField(max_length=100)
    clas_id = forms.CharField(max_length=100)


def new_classform(request):
    if request =='POST':
        form = Classes(request.POST)
        if form.is_vaild():
            print(form.cleaned.data)
            new_class = form.save()
            return HttpResponseRedirect('/ClassAdd' + str(new_class.pk))
        else:
            from = classform()
            return
    form = Classes()
    return render(request, 'create_class.html', {'form': form})
def classes_list(request):
    if request == 'POST':
        if form.is_vaild():
            new_class = form.save()
'''