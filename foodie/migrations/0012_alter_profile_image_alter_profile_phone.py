# Generated by Django 4.0.2 on 2022-02-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0011_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profile-icon.jpg', null=True, upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
