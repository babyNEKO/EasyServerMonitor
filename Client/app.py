from flask import Flask, render_template, jsonify, request, redirect, url_for
from ESM_Plugin.HostStatus import cpu_info, memory_info, disk_info, system_info, network_info, services_info
from os import listdir, mkdir
from os.path import exists, join as os_path_join
from werkzeug.utils import secure_filename
from time import ctime

upload_folder = 'c:\\ESM_Client_Upload\\'
allowed_extensions = {'zip', 'rar', '7z', 'tar'}

ESM_Client = Flask(__name__)
ESM_Client.config['UPLOAD_FOLDER'] = upload_folder


def check_upload_folder():
    if upload_folder == '':
        return {'info': 'Not Set Upload Folder!', 'lv': 0}
    if upload_folder != '':
        if not exists(upload_folder):
            mkdir(upload_folder)
        if len(listdir(upload_folder)) == 0:
            return {'info': 'Without any files.', 'lv': 1}
        else:
            return {'info': listdir(upload_folder), 'lv': 2}


@ESM_Client.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        upload_file = request.files['file']
        if upload_file.filename != '':
            upload_file.save(os_path_join(upload_folder, secure_filename(upload_file.filename)))
        return redirect(url_for('index'))

    return render_template(
        'index.html',
        cpu_info=cpu_info(),
        ram_info=memory_info(),
        disk_info=disk_info(),
        system_info=system_info(),
        network_info=network_info(),
        services_info=services_info(),
        check_upload=check_upload_folder(),
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
        'Refresh_time': str(ctime()),
    }

    return jsonify(all_info)


if __name__ == '__main__':
    # test server, all IP address access, port 5000
    ESM_Client.debug = True
    ESM_Client.run(host='0.0.0.0')
