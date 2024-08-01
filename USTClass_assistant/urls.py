"""
URL configuration for USTClass_assistant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    # path("admin/", admin.site.urls),

    # 菜单界面
    path("menu/", views.menu),

    # 教室操作
    path("room/list/", views.room_list),
    path("room/appoint/", views.room_appoint),
    # path("room/maintainance/", views.room_maintanance),

    # 教学楼操作
    path("building/list/", views.building_list),

    # # 设备操作
    path("device/list/", views.device_list),
    # path("device/add/", views.device_add),
    path("device/<int:nid>/delete/", views.device_delete),
    # path("device/edit/", views.edit),

    # path("navigation/", views.navigation),

    # 数据库操作
    path("orm/", views.orm),
]
