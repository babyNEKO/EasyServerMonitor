from flask import Flask, render_template, jsonify
from ESM_Plugin.HostStatus import cpu_info, memory_info, disk_info, system_info, network_info, services_info

upload_folder = ''
allowed_extensions = {'zip', 'rar', '7z', 'tar'}

ESM_Client = Flask(__name__)
ESM_Client.config['UPLOAD_FOLDER'] = upload_folder


@ESM_Client.route('/')
def index():
    return render_template(
        'index.html',
        cpu_info=cpu_info(),
        ram_info=memory_info(),
        disk_info=disk_info(),
        system_info=system_info(),
        network_info=network_info(),
        services_info=services_info(),
    )


@ESM_Client.route('/All-info/', methods=['GET'])
def get_all_info():
    all_info = {
        'CPU': cpu_info(),
        'RAM': memory_info(),
        'DISK': disk_info(),
        'NETWORK': network_info(),
        'SYSTEM': system_info(),
        'SERVICES': services_info(),
    }

    return jsonify(all_info)


@ESM_Client.route('/receive_file/', methods=['POST'])
def receive_file():
    pass


if __name__ == '__main__':
    ESM_Client.debug = True
    ESM_Client.run(host='0.0.0.0')
