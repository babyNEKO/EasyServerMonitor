import requests
from time import ctime


def get_info(ip_address, port=5000):
    url = 'http://' + ip_address + ':' + str(port) + '/All-info/'

    context = {
        'ip_address': ip_address,
        'client_port': port,
        'cpuload': '',
        'ramload': '',
        'uptime': '',
        'status': '',
        'refresh_time': '',
    }

    try:
        response = requests.get(url=url, timeout=5)
        response.encoding = 'utf-8'

        context['cpuload'] = response.json()['CPU']['CPU_load']
        context['ramload'] = response.json()['RAM']['RAM_percent']
        context['uptime'] = response.json()['SYSTEM'][1]
        context['refresh_time'] = response.json()['Refresh_time']

        return context
    except requests.exceptions.ConnectionError:
        context['status'] = 'ClientConnectionError'
        return context
    except requests.exceptions.Timeout:
        context['status'] = 'ClientConnectionError'
        return context
    except KeyError:
        context['status'] = 'ClientAPIError'
        return context
# 2021年8月24日
