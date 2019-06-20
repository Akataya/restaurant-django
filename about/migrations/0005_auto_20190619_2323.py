# Generated by Django 2.2.2 on 2019-06-20 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='person_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='person_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]