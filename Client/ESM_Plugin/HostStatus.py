from psutil import virtual_memory
from psutil import disk_usage
from psutil import cpu_count


# doc:
# https://psutil.readthedocs.io/en/latest/

def cpu_info():
    host_cpu_info = {
        'CPU_core': cpu_count(logical=0),
        'CPU_logical': cpu_count(logical=1),
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
    host_disk_info = {

    }

    return host_disk_info


def network_info():
    pass


def services_info():
    pass


print(memory_info())
