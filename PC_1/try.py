import socket
import datetime
import time


# создаемTCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Привязываем сокет к порту
try:
    server_address = ('0.0.0.0', 10000)
    sock.bind(server_address)
except:
    server_address = ('0.0.0.0', 10001)
    sock.bind(server_address)
print('Старт сервера на {} порт {}'.format(*server_address))

# Слушаем входящие подключения
sock.listen(10)
# ждем соединения
print('Ожидание соединения...')
connection, client_address = sock.accept()
print('Подключено к:', client_address)
i=1
while True:   
    i=i+1
    connection.settimeout(4 )
    code = str(i)
    #print(code)
    str_print = f"Отправлено значение {code}."
    connection.send(code.encode())
    data = connection.recv(64)
    print(data.decode('utf-8', errors='ignore')[0:-2])
    time.sleep(2)
