# Generated by Django 4.0.2 on 2022-02-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='slug',
            field=models.SlugField(default='h', unique=True),
        ),
        migrations.AddField(
            model_name='variety',
            name='slug',
            field=models.SlugField(default='h', unique=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='image',
            field=models.ImageField(blank=True, default='variety.jpg', null=True, upload_to='variety'),
        ),
    ]
