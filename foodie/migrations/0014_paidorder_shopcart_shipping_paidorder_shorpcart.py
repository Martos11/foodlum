# Generated by Django 4.0.2 on 2022-02-22 11:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foodie', '0013_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaidOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('cart_no', models.CharField(blank=True, max_length=36, null=True)),
                ('payment_code', models.CharField(max_length=36)),
                ('paid_item', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'PaidOrder',
                'verbose_name_plural': 'PaidOrders',
                'db_table': 'PaidOrder',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('spicy', models.CharField(max_length=50)),
                ('order_no', models.CharField(max_length=36)),
                ('item_paid', models.BooleanField(default=False)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodie.meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Shopcart',
                'verbose_name_plural': 'Shopcarts',
                'db_table': 'ShopCart',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('spice', models.CharField(max_length=50)),
                ('shipping_no', models.CharField(max_length=50)),
                ('paid_cart', models.BooleanField(default=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('processing', 'processing'), ('shipping', 'shipping'), ('delivered', 'delivered')], default='new', max_length=50)),
                ('admin_remark', models.CharField(max_length=250)),
                ('paidorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodie.paidorder')),
            ],
            options={
                'verbose_name': ' Shipping',
                'verbose_name_plural': ' Shippings',
                'db_table': ' Shipping',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='paidorder',
            name='shorpcart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodie.shopcart'),
        ),
    ]