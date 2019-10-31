"""Attention
    Unable to use character except ASCII
"""

import socket
import chardet

class Client:

    def __init__(self, message):

        self.message = message

    def encode(self, code):

        if code == 'utf-8':
            self.code = code
            self.message_byte = self.message.encode('utf-8')

    def client(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # サーバを指定
            s.connect(('127.0.0.1', 50007))
            # サーバにメッセージを送る
            s.sendall(b'' + self.message_byte)
            # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
            data = s.recv(1024)
            #
            print(repr(data.decode('utf-8')))

if __name__ == '__main__':

    client = Client('いろはにほへと')
    client.encode('utf-8')
    client.client()
