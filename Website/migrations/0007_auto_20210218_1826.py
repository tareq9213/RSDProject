# Generated by Django 3.1.6 on 2021-02-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0006_auto_20210218_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsandevent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
