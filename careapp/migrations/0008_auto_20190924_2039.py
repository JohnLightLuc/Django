# Generated by Django 2.2.5 on 2019-09-24 20:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('careapp', '0007_auto_20190924_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubscription',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formsubscription',
            name='date_up',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
