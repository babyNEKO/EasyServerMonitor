from flask import Flask, render_template, jsonify
from ESM_Plugin.HostStatus import cpu_info, memory_info, disk_info
from ESM_Plugin import SendStatus

ESM_Client = Flask(__name__)


@ESM_Client.route('/')
def index():
    return render_template(
        'index.html',
        cpu_info=cpu_info(),
        ram_info=memory_info(),
        disk_info=disk_info()
    )


@ESM_Client.route('/All-info/', methods=['GET'])
def get_all_info():
    all_info = {
        'CPU': cpu_info(),
        'RAM': memory_info(),
        'DISK': disk_info(),
    }

    return jsonify(all_info)


if __name__ == '__main__':
    ESM_Client.run()

