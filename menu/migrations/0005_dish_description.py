# Generated by Django 2.2.2 on 2019-06-19 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20190619_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='description',
            field=models.TextField(max_length=100, null=True),
        ),
    ]