# Generated by Django 2.2.2 on 2019-06-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190619_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='default_article.jpg', upload_to='articles/'),
        ),
    ]
