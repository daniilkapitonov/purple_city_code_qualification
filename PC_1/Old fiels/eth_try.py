#test-server.py
import socket
import sys
import time
from multiprocessing import Process
import multiprocessing
import random

def new_client(num_of_connection, connection, client_address):
    num_of_con = num_of_connection.value
    f = open("txt_files/txt_f_con_"+str(num_of_con)+".txt", "w", encoding= "UTF-8")
    f.close()
    str_print = ""
    str_print +=f"Номер соединения - {num_of_con}" + ' '
    #print(f"Номер соединения - {num_of_connection}")
    check_connection = True
    while check_connection:
        err = 0
        for i in range(10,99):
            #str_print+=f"Отправлена цифра - {i}"+' '
            #print(f"Отправлена цифра - {i}")
            #connection.send(str(i).encode())
            str_send = ""
            for z in range(1,8):
                str_send += str(random.randint(0,1))
            str_print+=f"Отправлено - {str_send}"+' '
            connection.send(str(str_send).encode())
            connection.settimeout(8)
            try:
                data = connection.recv(64)
            except Exception:
                str_print+="ТаймАут "
                #print("ТаймАут")
                data = "".encode()
            
            
            if not data:
                err += 1
                str_print +=f"Ответ {num_of_con} не получен"+' '
                #print(f"Ответ {num_of_connection} не получен")
                if err == 5:
                    check_connection = False
                    break
            else:
                f = open("txt_files/txt_f_con_"+str(num_of_con)+".txt", "a", encoding= "UTF-8")
                str_print+=f"Ответ {num_of_con} получен. Получено - "+data.decode('utf-8', errors='ignore')+' '
                #str_in_f = str(data.decode('utf-8', errors='ignore'))[0] + str(data.decode('utf-8', errors='ignore'))[1]
                #f.write(str_in_f+'\n')
                f.close()
                #print(f"Ответ {num_of_connection} получен. Получено - "+data.decode('utf-8', errors='ignore'))
            print(str_print)
            str_print = ""
            time.sleep(1)
    
    print(f"Соединение {num_of_con} {client_address} прервано")
    with num_of_connection.get_lock():
        num_of_connection.value -=1
    connection.close()

if __name__ == '__main__':
    # создаемTCP/IP сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Привязываем сокет к порту
    server_address = ('0.0.0.0', 10001)
    print('Старт сервера на {} порт {}'.format(*server_address))
    sock.bind(server_address)

    # Слушаем входящие подключения
    sock.listen(100)
    proc = []
    num_of_connection = multiprocessing.Value('i',1)
    while True:   
        # ждем соединения
        if num_of_connection.value < 3:
            print('Ожидание соединения...')
            connection, client_address = sock.accept()
            print('Подключено к:', client_address)
            # Принимаем данные порциями и ретранслируем их
            new_proc = Process(target = new_client, args = (num_of_connection, connection, client_address))
            proc.append(new_proc)
            new_proc.start()
            time.sleep(1)
            num_of_connection.value += 1
        else:
            print("Все соединения заняты")
            f = open("txt_files/txt_f_con_1.txt", "r", encoding= "UTF-8")
            print(f.read())
            f.close()
            time.sleep(10)

        
