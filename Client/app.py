from flask import Flask, render_template
from ESM_Plugin import HostStatus
from ESM_Plugin import SendStatus

ESM_Client = Flask(__name__)


@ESM_Client.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    ESM_Client.run()
