# Generated by Django 2.2.2 on 2019-06-20 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(),
        ),
    ]
