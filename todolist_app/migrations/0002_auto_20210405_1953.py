# Generated by Django 2.0 on 2021-04-05 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priority',
            name='orden',
        ),
        migrations.AddField(
            model_name='priority',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
