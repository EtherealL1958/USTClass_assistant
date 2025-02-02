# Generated by Django 5.0.6 on 2024-07-30 09:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0003_alter_room_add_info"),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="add_info",
            field=models.TextField(default="无", verbose_name="备注"),
        ),
        migrations.AlterField(
            model_name="building",
            name="location",
            field=models.TextField(default="无", verbose_name="教学楼地址"),
        ),
        migrations.RemoveField(
            model_name="room",
            name="device_list",
        ),
        migrations.AlterField(
            model_name="room",
            name="status",
            field=models.SmallIntegerField(
                choices=[(1, "空闲"), (2, "上课使用"), (2, "临时借用"), (3, "考试使用")],
                verbose_name="状态",
            ),
        ),
        migrations.AddField(
            model_name="room",
            name="device_list",
            field=models.ManyToManyField(to="app01.device", verbose_name="设备"),
        ),
    ]
