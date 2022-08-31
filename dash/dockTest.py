# # from docker import APIClient
# # from docker import DockerClient
# # clientT = DockerClient(base_url='tcp://192.168.4.90:5000', tls=True)
# # clientT.containers()
# # # client=APIClient(base_url=)
# # import docker
# # client = docker.from_env()
# # var = client.images
# # import os
# # size = 0
# # for i in os.scandir('/home/afnan/PycharmProjects/CodingManiac/dash'):
# #     size+=os.path.getsize(i)
# #     print(os.path.getsize(i))
# # print(size)
#
# print(0.1*1000000)
from os import abort

from flask import Flask, send_from_directory, send_file

app = Flask(__name__)
# Specify directory to download from . . .
DOWNLOAD_DIRECTORY = "/home/afnan/PycharmProjects/CodingManiac/dash/dash_4.py"

@app.route('/get-files/down',methods = ['GET','POST'])
def get_files():

    """Download a file."""
    try:
        return send_file(DOWNLOAD_DIRECTORY)
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000, threaded = True, debug = False)