from psutil import virtual_memory
from psutil import disk_usage, disk_partitions
from psutil import cpu_count, cpu_percent
from datetime import datetime
from psutil import boot_time
from psutil import net_if_stats, net_if_addrs


# doc:
# https://psutil.readthedocs.io/en/latest/

def cpu_info():
    host_cpu_info = {
        'CPU_core': cpu_count(logical=0),
        'CPU_logical': cpu_count(logical=1),
        'CPU_load': cpu_percent(percpu=1),
    }

    return host_cpu_info


def memory_info():
    host_memory_info = {
        'RAM_total': virtual_memory().total // 1024 // 1024,
        'RAM_available': virtual_memory().available // 1024 // 1024,
        'RAM_percent': virtual_memory().percent,
        'RAM_used': virtual_memory().used // 1024 // 1024,
        'RAM_free': virtual_memory().free // 1024 // 1024,
    }

    return host_memory_info


def disk_info():
    disk_symbol = []
    for i in disk_partitions():
        disk_symbol.append(i.device.replace('\\', ''))

    host_disk_info = []
    count = 0
    for j in disk_symbol:
        host_disk_info.append({
            'device': j,
            'mnt': disk_partitions()[count].device.replace('\\', ''),
            'fstype': disk_partitions()[count].fstype,
            'total': disk_usage(path=j).total // 1024 // 1024,
            'used': disk_usage(path=j).used // 1024 // 1024,
            'free': disk_usage(path=j).free // 1024 // 1024,
            'percent': disk_usage(path=j).percent,
        })
        count += 1

    return host_disk_info


def network_info():
    host_network_info = []

    return host_network_info


def services_info():
    pass


def system_info():
    host_system_info = {
        'boot_time': datetime.fromtimestamp(boot_time()).strftime('%Y-%m-%d %H:%M:%S'),
    }
    return host_system_info

