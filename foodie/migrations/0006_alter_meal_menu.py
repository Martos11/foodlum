# Generated by Django 4.0.2 on 2022-02-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0005_meal_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='menu',
            field=models.TextField(),
        ),
    ]
