from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
import datetime

class Registrationform(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(required=True)

class Meta:
    model = User
    fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',
    )
    def save(self, commit=True):
        user = super(Registrationform,self).save(commit=True)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            return user


class BlogApp(forms.ModelForm):

    title = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder':'Title','class':'form-control'}))
    date_created = forms.DateField(widget=forms.DateTimeField()),
    text = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'placeholder':'Text','class':'form-control'}))


    class Meta:
        model = Blog
        fields = ('title','text',)