# Generated by Django 2.2.2 on 2019-06-22 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactdetails',
            old_name='emails',
            new_name='email',
        ),
    ]
