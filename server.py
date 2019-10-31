import socket

class Server:

    def __init__(self):

        self.dict = {'山': '川',
                      '努力': '根性',
                      'いろはにほへと': 'うぬのおくやま',
                      '銀河': '多摩川'}

    def server(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # IPアドレスとポートを指定
            s.bind(('127.0.0.1', 50007))
            # 1 接続
            s.listen(1)
            # connection するまで待つ
            while True:

                print('Now listening... ')
                # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
                conn, addr = s.accept()
                with conn:
                    while True:
                        # データを受け取る
                        data = conn.recv(1024)
                        if not data:
                            break
                        # クライアントにデータを返す(b -> byte でないといけない)
                        conn.sendall(b'' + self.dict[data.decode('utf-8')].encode('utf-8'))

if __name__ == '__main__':

    server = Server()
    server.server()
