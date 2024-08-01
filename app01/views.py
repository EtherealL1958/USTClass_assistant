from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django import forms
# Create your views here.
def menu(request):
    return render(request, "menu.html")

def room_list(request):
    if request.method == 'GET':
        queryset = models.Room.objects.all()
        return render(request, "room_list.html", {"queryset": queryset})
    
class AppointModelForm(forms.ModelForm):
    class Meta:    # 固定名称：Meta，首字母不可小写
        model = models.Appointment         # 固定名称
        # 需要添加字段时在这添加
        fields = ["appoint_type", "appoint_info", "appoint_room", "start_time", "end_time"]
        # 一种自动添加css样式的方法：widgets插件
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.PasswordInput(attrs={"class": "form-control"}),
        #     "age": forms.TextInput(attrs={"class": "form-control"}),
        # }
    
    # 另外一种添加样式的方法：重定义__init__()
    def __init__(self, *args, **kwargs):
        # 执行父类的__init__()方法
        super().__init__(*args, **kwargs)

def room_appoint(request):
    if request.method == 'GET':
        # 获取通过url上传递过来的id（如果有的话）
        room_id = request.GET.get('nid')

        # 设置初始值
        initial_data = {}
        if room_id:
            initial_data['appoint_room'] = room_id
            
        form = AppointModelForm(initial=initial_data)
        return render(request, "room_appoint.html", {"form": form})
    
    form = AppointModelForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("成功")
    else:
        return render(request, "room_appoint.html", {"form": form})

# def room_maintainance(request):

def building_list(request):
    if request.method == 'GET':
        queryset = models.Building.objects.all()
        return render(request, "building_list.html", {"queryset": queryset})


def device_list(request):
    if request.method == 'GET':
        queryset = models.Device.objects.all()
        return render(request, "device_list.html", {"queryset": queryset})
    
def device_add(request):
    pass
    
def device_delete(request, nid):
    models.Device.objects.filter(id=nid).first().delete()
    return redirect("/device/list/")
    


# def device_add(request):


# def device_delete(request):


# def device_edit(request):


# def navigation(request):
        
from .models import Room, Device, Building
def orm(request):
    # 创建ManyToMany关系：
    # bu = Building.objects.filter(id=1).first()
    # Room.objects.create(name="1115",type=3,size=20,building=bu)
    # Room.objects.filter(id=4).first().device_list.add(1,2,3,4)

    return HttpResponse("成功")
