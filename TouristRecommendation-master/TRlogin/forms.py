

from attr import attrs
from django import forms
from ipywidgets.widgets import widget

class UserForm(forms.Form):
    username = forms.CharField(label="",max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="",max_length=128,widget=forms.PasswordInput(attrs={'class':'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名",max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="密码",max_length=128,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="确认密码",max_length=128,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class':'tr_tags'}),
    #                     choices=(
    #                               ("上海", "上海"),
    #                               ("云南", "云南"),
    #                               ("广东", "广东"),
    #                              ))