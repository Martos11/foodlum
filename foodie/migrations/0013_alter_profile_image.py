# Generated by Django 4.0.2 on 2022-02-21 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0012_alter_profile_image_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='bolz.jpg', null=True, upload_to='profile'),
        ),
    ]
