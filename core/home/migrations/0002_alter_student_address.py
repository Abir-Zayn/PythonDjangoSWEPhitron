# Generated by Django 4.2.4 on 2023-08-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    #!If we remove the dependencies (migaration file) the database will collapse. As its depend on the 0001_initial_py
    dependencies = [
        ('home', '0001_initial'),
    ]

    # It will check top to buttom in the model to detect the changes.following makemigration do migrate 
    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
