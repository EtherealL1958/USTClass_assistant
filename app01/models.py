from django.db import models
from django.core.exceptions import ValidationError

# 操作时间
from django.utils import timezone
from datetime import timedelta

# Create your models here.

# 教学楼
class Building(models.Model):
    name = models.CharField(verbose_name="教学楼名称", max_length=20)
    info = models.TextField(verbose_name="教学楼简介")
    location = models.TextField(verbose_name="教学楼地址", default="无")


# 房间
class Room(models.Model):
    type_choices = (
        (1, "普通教室"),
        (2, "艺术教室"),
        (3, "研讨室"),
        (4, "多媒体教室"),
        (5, "实验室"),
        (6, "其他"),
    )

    status_choices = (
        (1, "空闲"),
        (2, "上课使用"),
        (3, "临时借用"),
        (4, "考试使用"),
    )

    name = models.CharField(verbose_name="教室名称", max_length=20)
    type = models.SmallIntegerField(verbose_name="教室类型", choices=type_choices)
    building = models.ForeignKey(verbose_name="所属教学楼", to="Building", to_field="id", on_delete=models.CASCADE)
    size = models.IntegerField(verbose_name="容量")
    device_list = models.ManyToManyField(verbose_name="设备", to="Device", blank=True)
    # images = models.ImageField(verbose_name="参考图片")
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    add_info = models.TextField(verbose_name="备注", default="无")

    def __str__(self):
        return self.name


# 设备
class Device(models.Model):
    type_choices = (
        (1, "空调"),
        (2, "电脑"),
        (3, "白板系统"),
        (4, "音箱"),
        (5, "实验仪器"),
        (6, "其他"),
    )
    name = models.CharField(verbose_name="设备名", max_length=20)
    type = models.SmallIntegerField(verbose_name="设备类型", choices=type_choices)
    add_info = models.TextField(verbose_name="备注", default="无")


# 预约记录
class Appointment(models.Model):
    appoint_type_choices = (
        (2, "上课使用"),
        (3, "临时借用"),
        (4, "考试使用"),
    )
    appoint_type = models.SmallIntegerField(verbose_name="预约类型", choices=appoint_type_choices, null=True)
    appoint_info = models.CharField(verbose_name="预约原因及用途", max_length=100)
    appoint_room = models.ForeignKey(verbose_name="预约教室", to="Room", to_field="id", on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")

    # 验证方法clean
    def clean(self):
        # 确保结束时间在开始时间之后
        if self.end_time <= self.start_time:
            raise ValidationError('结束时间必须在开始时间之后')
        
        mininum_duration = timedelta(minutes=30)
        if self.end_time - self.start_time <= mininum_duration:
            raise ValidationError("预约时长不可小于30分钟")
    
    # 预约人信息从登录端口获取

