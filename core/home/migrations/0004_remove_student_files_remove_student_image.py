# Generated by Django 4.2.4 on 2023-08-20 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_student_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='files',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
