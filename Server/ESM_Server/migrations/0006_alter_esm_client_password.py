# Generated by Django 3.2.5 on 2021-08-21 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESM_Server', '0005_alter_esm_client_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esm',
            name='client_password',
            field=models.CharField(default='None', max_length=1024, null=True, verbose_name='密码'),
        ),
    ]
