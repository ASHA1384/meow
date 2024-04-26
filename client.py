import socket
from util import Config, read_config_data
import threading


def register():
    m = input('for login Enter 1|for sign up Enter 2 : ')
    if m == '1':
        client.send('login'.encode(config_object.encoding))
        username = input('Enter your username : ')
        client.send(username.encode(config_object.encoding))
        password = input('Enter your password : ')
        client.send(password.encode(config_object.encoding))
        a = client.recv(1024).decode(config_object.encoding)
        if a == 'login was successful!':
            print(a)
        else:
            while True:
                print(a)
                username = input('Enter your username : ')
                client.send(username.encode(config_object.encoding))
                password = input('Enter your password : ')
                client.send(password.encode(config_object.encoding))
                v = client.recv(1024).decode(config_object.encoding)
                if v == 'login was successful!':
                    print(v)
                    break
    elif m == '2':
        client.send('sign up'.encode(config_object.encoding))
        username = input('Enter your username : ')
        client.send(username.encode(config_object.encoding))
        password = input('Enter your password : ')
        client.send(password.encode(config_object.encoding))
        m = client.recv(1024).decode(config_object.encoding)
        if m == 'info already exists.change your username or password please.':
            print(m)
            while True:
                un = input('Enter your username : ')
                p = input('Enter your password : ')
                client.send(un.encode(config_object.encoding))
                client.send(p.encode(config_object.encoding))
                mes = client.recv(1024).decode(config_object.encoding)
                if mes == 'info already exists.change your username or password please.':
                    print(mes)
                else:
                    print(mes)
                    break
        else:
            print(m)


def chat():
    while True:
        m = '{}: {}'.format(name, input())
        client.send(m.encode(config_object.encoding))


def receive():
    while True:
        m = client.recv(1024).decode(config_object.encoding)
        print(m)


if __name__ == '__main__':
    config_data = read_config_data()
    config_object = Config(config_data)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((config_object.host, config_object.port))

    name = input('Enter your name skinny bitch : ')
    client.send(name.encode(config_object.encoding))
    message = client.recv(1024).decode('ascii')
    print(message)
    register()
    t = threading.Thread(target=chat)
    t.start()
    t_1 = threading.Thread(target=receive)
    t_1.start()
