# Generated by Django 3.2.5 on 2021-08-21 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESM_Server', '0002_auto_20210820_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='esm',
            name='pin_to_index',
            field=models.BooleanField(default=False, verbose_name='固定到主页'),
        ),
    ]
