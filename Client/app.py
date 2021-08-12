from flask import Flask, render_template
from ESM_Plugin import HostStatus
from ESM_Plugin import SendStatus

ESM_Client = Flask(__name__)


@ESM_Client.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    ESM_Client.run()
