# Generated by Django 2.2.5 on 2019-09-24 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0006_auto_20190924_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formappointment',
            name='docteur',
            field=models.CharField(max_length=50),
        ),
    ]
