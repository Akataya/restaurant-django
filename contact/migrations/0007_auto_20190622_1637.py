# Generated by Django 2.2.2 on 2019-06-22 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_scheduleitem_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleitem',
            name='close_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='scheduleitem',
            name='open_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
