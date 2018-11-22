from django.http import HttpResponse
from django.shortcuts import render
from hellodjango.models import Student

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from hellodjango.serializers import UserSerializer, GroupSerializer, StudentSerializer
from hellodjango.forms import loginForm,StudentForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the hellodjango index.")


def hello(request):
    return HttpResponse("Hello Python!")



def detail(request,sid):
    m = Student.objects.get(id=sid);
    # print(m.get_sex_display())
    return render(request,'../templates/hello.html',{'id':m.id,'name':m.name,'sex':m.sex,'addr':m.addr})

def student_detail(request,ssid):
    m = Student.objects.get(id=ssid);
    return render(request,'../templates/hello.html',{'id':m.id,'name':m.name,'sex':m.sex,'addr':m.addr})




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stuents to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



def register(request):
    form_obj = loginForm()
    if request.method=='POST':
        form_obj = loginForm(request.POST)
        if form_obj.is_valid():
            return HttpResponse("注册成功")

    return render(request,'../templates/login.html',{"form_obj":form_obj})


def saveStudent(request,id):

    student = Student.objects.get(pk=id)
        #obj = studentForm()
    if request.method=='POST':
        obj = studentForm(request.POST, instance=student)

        print(obj.is_valid())
        # print(obj.name)
        # print(obj.cleaned_data)
        # print(obj.createDate)
        if obj.is_valid():
            print(obj)
            obj.save()
        else:
            print(123)
            print(obj.errors)
    else:
        obj = studentForm(instance=student)
    return render(request, '../templates/student.html', {"obj": obj})


def studentList(request):
    li = Student.objects.all()
    return render(request, '../templates/studentList.html', {"li":li})

def editStudent(request,nid):
    if request.method == "GET":
        print('123')
        student_obj = Student.objects.filter(id=nid).first()
        sf = studentForm(instance=student_obj)
        return render(request, '../templates/studentEdit.html', {"sf":sf,"nid":nid})

    else:
        print("Post")
        student_obj = Student.objects.filter(id=nid).first()
        sf = studentForm(request.POST,instance=student_obj)
        print(sf.is_valid())
        if sf.is_valid():
            print('234')
            sf.save()
            print("保存成功！")
        else:
            print('345')
            print(sf.errors.as_json())
        return render(request, '../templates/studentEdit.html',{"sf":sf,"nid":nid})



def delStudent(request,nid):
    if request.method=='POST':
        return HttpResponse(nid+"删除成功!")
    elif request.method == 'GET':
        print("GET")
        Student.objects.filter(id=nid).delete()
        print('删除成功！')
        li = Student.objects.all()
        return render(request, '../templates/studentList.html', {"li": li})


