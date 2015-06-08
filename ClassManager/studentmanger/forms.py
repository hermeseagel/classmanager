from django import forms
from django.core.exceptions import ValidationError
from .models import classes

class ClassForm(forms.ModelForm):
    class Meta:
        model = classes
        fields = ('class_name','class_id','class_loc')
#   classname = forms.CharField(max_length=100)
#   class_loc = forms.CharField(max_length=100)
#     def __init__(self, *args, **kwargs):
  #      super(ClassForm, self).__init__(*args, **kwargs))
  #      self.fields['clssname'].required = True
#from .models import Post

#class PostForm(forms.ModelForm):

#    class Meta:
#        model = Post
#        fields = ('title', 'text')