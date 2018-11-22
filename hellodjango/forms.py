from django.forms import ModelForm
from django import forms

from hellodjango.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name','sex','addr','id']
        labels = {
            'id':'序号',
        }
        error_messages = {
            'name': {
                'max_length': ("This writer's name is too long."),
            },
            'sex': {
                'max_length': ("This writer's name is too long."),
            },
            'addr': {
                'max_length': ("This writer's name is too long."),
            },

        }



class loginForm(forms.Form):
    name = forms.CharField(label='用户名',initial='张三')
    pwd = forms.CharField(min_length=6,label='密码')


