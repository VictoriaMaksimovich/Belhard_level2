"""

написать приложение-клиент используя модуль socket работающее в домашней 
локальной сети.
Приложение должно соединятся с сервером по известному адрес:порт и отправлять 
туда текстовые данные.

известно что сервер принимает данные следующего формата:
    "command:reg; login:<login>; password:<pass>" - для регистрации пользователя
    "command:signin; login:<login>; password:<pass>" - для входа пользователя
    
    
с помощью программы зарегистрировать несколько пользователей на сервере и произвести вход


"""

import socket

sock = socket.socket()

HOST = ('127.0.0.1', 7777)

sock.connect(HOST)

# sock.send(b"command:reg; login:alfa11; password:zxc12345")
# sock.send(b"command:reg; login:beta22; password:vbn45678")
# sock.send(b"command:reg; login:gamma33; password:qwerty")

