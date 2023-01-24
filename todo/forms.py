from email.policy import default
from django.forms import ModelForm
from django import forms
from .models import Project, Comment
 
class ProjectForm(ModelForm):
     
    class Meta:
        model = Project
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('__all__')