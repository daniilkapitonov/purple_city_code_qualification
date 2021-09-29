#test-server.py
import socket
import sys
import time
from multiprocessing import Process
import multiprocessing
import random
import datetime

def new_client(num_of_connection, connection, client_address):
    num_of_con = num_of_connection.value
    str_print = ""
    err=0
    str_print +=f"Номер соединения - {num_of_con}" + ' '
    #print(f"Номер соединения - {num_of_connection}")
    #1 - принимает, 2 - отравляет
    check_connection = True
    while check_connection:
        #try:
        data = connection.recv(64)
        print(data.decode('utf-8', errors='ignore'))
        if int(data.decode('utf-8', errors='ignore')) ==1 or int(data.decode('utf-8', errors='ignore')) == 2: 
            connection.send("1".encode())
            check_connection = False
    check_connection = True
    print(str_print)
    if check_connection:
        if int(data.decode('utf-8', errors='ignore')) == 1:
            str_print += f"Cоединение - {num_of_con}. Установлен режим работы - принимающий."
            print (str_print)
            str_print=""
            while check_connection:
                f = open("/home/pi/Desktop/Demo/txt_files/send_message.txt", 'r')
                code = str(f.read())
                #print(code)
                str_print = f"Отправлено значение {code}. По соединению № {num_of_con}."
                f.close()
                try:
                    connection.send(code.encode())
                except Exception:
                    str_print+="Устройство не отвечает"
                    #print("ТаймАут")
                    err+=1
                    data = "".encode()
                connection.settimeout(4 )
                try:
                    data = connection.recv(64)
                except Exception:
                    str_print+="Устройство не отвечает"
                    #print("ТаймАут")
                    err+=1
                    data = "".encode()
                if err == 5:
                    err = 0
                    check_connection = False
                print(str_print)
                if err == 0:
                    time.sleep(10)
                else: 
                    time.sleep(2)
        else:
            if int(data.decode('utf-8', errors='ignore')) == 2:
                str_print += f"Cоединение - {num_of_con}. Установлен режим работы - отправляющий."
                print (str_print)
                str_print=""
                while check_connection:
                    connection.settimeout(4)
                    try:
                        data = connection.recv(64)
                        str_resive = data.decode('utf-8', errors='ignore')
                        str_check = True
                    except Exception:
                        str_print+="Устройство не отвечает"
                        #print("ТаймАут")
                        err+=1
                        data = "".encode()
                        str_resive = "_ _ _ "
                        str_check = False
                    
                    str_print = f"Получено значение {str_resive}. По соединению № {num_of_con}."
                    num_1 = str_resive.split("_")[0]
                    num_2 = str_resive.split("_")[1]
                    num_3 = str_resive.split("_")[2]
                    #print (num_1, num_2, num_3)
                    #1 - время наработки 2 - энергии потрачено (амперы) 3 - эенергии получено (амперы) 
                    #4 - энергии в хранилище в проценах 5 - время дня в часах
                    data = datetime.datetime.now()
                    data = data.strftime("%H")
                    #print(data)
                    total_time = "6"
                    if str_check:
                        f = open ("/home/pi/Desktop/Demo/txt_files/data_for_web.txt", "w")
                        f.write(total_time +'\n' + num_1+'\n'+num_2+'\n'+num_3+'\n'+data)
                        f.close()
                    if err == 5:
                        err = 0
                        check_connection = False
                    print(str_print)
                    if err == 0:
                        time.sleep(5)
                    else: 
                        time.sleep(1)
            else:
                str_print += "Код устройства не найден в базе. Отключение."
                check_connection = False
    
    print(f"Соединение {num_of_con} {client_address} прервано")
    with num_of_connection.get_lock():
        num_of_connection.value -=1
    connection.close()

if __name__ == '__main__':
    # создаемTCP/IP сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Привязываем сокет к порту
    server_address = ('0.0.0.0', 10000)
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
            # f = open("txt_files/txt_f_con_1.txt", "r", encoding= "UTF-8")
            # print(f.read())
            # f.close()
            time.sleep(10)

        
