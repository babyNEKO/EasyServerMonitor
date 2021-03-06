# Generated by Django 3.2.5 on 2021-08-20 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ESM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=24, unique=True, verbose_name='IP地址')),
                ('client_port', models.IntegerField(default=5000, verbose_name='端口')),
                ('boot_time', models.CharField(default='', max_length=128, verbose_name='Boot Time')),
                ('login_users', models.CharField(default='', max_length=128, verbose_name='Login Users')),
                ('cpu_core', models.CharField(max_length=128, verbose_name='CPU Core')),
                ('cpu_load', models.CharField(max_length=128, verbose_name='CPU Load')),
                ('ram_total', models.IntegerField(verbose_name='RAM Total')),
                ('ram_used', models.CharField(max_length=128, verbose_name='RAM Used')),
                ('ram_free', models.CharField(max_length=128, verbose_name='RAM Free')),
                ('ram_available', models.CharField(max_length=128, verbose_name='RAM Available')),
                ('ram_percent', models.CharField(max_length=128, verbose_name='RAM Percent')),
            ],
        ),
    ]
