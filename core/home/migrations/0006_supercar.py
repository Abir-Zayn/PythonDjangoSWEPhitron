# Generated by Django 4.2.4 on 2023-08-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_car_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='superCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_car_brand', models.CharField(max_length=100)),
                ('s_car_speed', models.IntegerField(default=20)),
            ],
        ),
    ]
