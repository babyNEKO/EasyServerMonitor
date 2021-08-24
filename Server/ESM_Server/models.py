from django.db import models


class ESM(models.Model):
    # 客户端基础信息
    ip_address = models.CharField(verbose_name='IP地址', max_length=24, unique=True, null=False)
    client_port = models.IntegerField(verbose_name='端口', default=5000, null=False)
    client_password = models.CharField(verbose_name='密码', max_length=1024, null=True, default='None')
    pin_to_index = models.BooleanField(verbose_name='固定到主页', default=False)
    # 客户端基础信息 -- end

    def __str__(self):
        return str(self.ip_address)
