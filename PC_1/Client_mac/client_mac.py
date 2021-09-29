import socket #dla tsp serverov
import sys
import time
from multiprocessing import Process
import multiprocessing
import random
import datetime
import os

adm_house_file = r"администрация.txt" #3 +
batary_file = r"батареи.txt" #1 
hospital_house_file = r"больница.txt" #3 +
water_file = r"вода.txt" #1
energy_generate_file = r"выработка.txt" #1 +
house_1_file = r"дом_1.txt" #4 +
house_2_file = r"дом_2.txt" #4 +
house_all_file = r"дома.txt" #2 +
buildings_all_file = r"здания.txt" #3 +
mchs_file = r"мчс.txt" #3 +
energy_consumption_file = r"потребление.txt" #1 +
ges_state_file = r"ges_s.txt" #1 +
output_file = r"output.txt" #3 +
pred_file = r"pred.txt" #3 +

adm_rele_file = r"administration.txt" #4 +
hospital_rele_file = r"hospital.txt" #5 +
house_1_rele_file = r"house_1.txt" #7 +
house_2_rele_file = r"house_2.txt" #7 +
mchs_rele_file = r"mus.txt" #5 +
ges_rele_file = r"ges.txt" #5 + 
car_move_file = r"move_comand.txt"

file_list = ["администрация.txt", "батареи.txt", "больница.txt", "вода.txt","выработка.txt", "дом_1.txt", "дом_2.txt",
     "дома.txt","здания.txt", "мчс.txt","потребление.txt", "ges_s.txt", "output.txt", "pred.txt","administration.txt", 
     "hospital.txt", "house_1.txt", "house_2.txt", "mus.txt", "ges.txt", "move_comand.txt"]
os.chdir("Client_mac")
root_c = []
i=0
for root, dirs, files in os.walk(os.getcwd()):
    root_c.append(root)
root_c.pop(0)
for root in root_c:
    for root1, dirs1,files1 in os.walk(root):
        for file  in files1:
            if file in file_list and os.path.isfile(root+"/"+file):
                o=1
                #print("Я нашёл файл - ", file, ". По пути - ", os.path.abspath(root1+"/"+file))
                if file in adm_house_file:
                    adm_house_file = os.path.abspath(root1+"/"+file)
                if file in batary_file:
                    batary_file = os.path.abspath(root1+"/"+file)
                if file in hospital_house_file:
                    hospital_house_file = os.path.abspath(root1+"/"+file)
                if file in water_file:
                    water_file = os.path.abspath(root1+"/"+file)
                if file in energy_generate_file:
                    energy_generate_file = os.path.abspath(root1+"/"+file)
                if file in house_1_file:
                    house_1_file = os.path.abspath(root1+"/"+file)
                if file in house_2_file:
                    house_2_file = os.path.abspath(root1+"/"+file)
                if file in house_all_file:
                    house_all_file = os.path.abspath(root1+"/"+file)
                if file in buildings_all_file:
                    buildings_all_file = os.path.abspath(root1+"/"+file)
                if file in mchs_file:
                    mchs_file = os.path.abspath(root1+"/"+file)
                if file in energy_consumption_file:
                    energy_consumption_file = os.path.abspath(root1+"/"+file)
                if file in ges_state_file:
                    ges_state_file = os.path.abspath(root1+"/"+file)
                if file in output_file:
                    output_file = os.path.abspath(root1+"/"+file)
                if file in pred_file:
                    pred_file = os.path.abspath(root1+"/"+file)
                if file in adm_rele_file:
                    adm_rele_file = os.path.abspath(root1+"/"+file)
                if file in hospital_rele_file:
                    hospital_rele_file = os.path.abspath(root1+"/"+file)
                if file in house_1_rele_file:
                    house_1_rele_file = os.path.abspath(root1+"/"+file)
                if file in house_2_rele_file:
                    house_2_rele_file = os.path.abspath(root1+"/"+file)
                if file in mchs_rele_file:
                    mchs_rele_file = os.path.abspath(root1+"/"+file)
                if file in ges_rele_file:
                    ges_rele_file = os.path.abspath(root1+"/"+file)
                i+=1
if i != len(file_list):
    print ("ERROR Кол-во файлов в массиве и директории", os.getcwd()," не совпадает")



#os.chdir(r"Client_mac/")
print(os.getcwd())
f = open (batary_file, "r")
print(f.read())
f.close()
print("Подключение к северу")
sock = socket.socket()
sock.connect(('192.168.0.100', 10000))
identification = True
check_connection = True
print("Подключено к серверу")
err_count = 0
while identification:
    sock.settimeout(4)
    try:
        data = sock.recv(64)
        data = str(data.decode('utf-8', errors='ignore'))
    except BaseException:
        data = "err"
        err_count += 1
    data = data.replace("_","")
    if "666" in data:
        print("Запрос режима работы")
        sock.send("macbook".encode())
        try:
            data = sock.recv(64)
            data = str(data.decode('utf-8', errors='ignore'))
        except BaseException:
            data = "err"
            err_count += 1
        if "167" in data:
            identification = False
            print("Идентификация прошла успешно")
    elif err_count > 4:
        identification = False
        check_connection = False
        print("Идентификация не прошла успешно")

while check_connection:
    sock.settimeout(5)
    try:
        data = sock.recv(256)
        data = str(data.decode('utf-8', errors='ignore'))
    except BaseException:
        data = "err"
        err_count += 1
    sock.send("12".encode())
    if not "sendme" in data:
        data = ''
        sock.settimeout(5)
        try:
            data = sock.recv(256)
            data = str(data.decode('utf-8', errors='ignore'))
        except BaseException:
            data = "err"
            err_count += 1
        print(data)
        data_in = data.split("__")[0].replace(" ", "\n")
        data_f_p = data.split("__")[1]
        print(data_in, data_f_p)
        sock.send("12".encode())
        # try:
        #     data = sock.recv(256)
        #     data = str(data.decode('utf-8', errors='ignore'))
        # except BaseException:
        #     data = "err"
        #     err_count += 1
        # data_f_p = data
        # print(data_f_p)
        f = open(data_f_p, "w")
        f.write(data_in)
        f.close()
        #sock.send(data.encode())
    else:
        # for root, dirs, files in os.walk(r"Данные"):
        #     for f_name in files:
        #         print (str(root+"/"+f_name))
        #         sock.send(str(root+"/"+f_name).encode())
        #         time.sleep(0.2)
        # sock.send("finish".encode())
        # data = ""
        try:
            data = sock.recv(256)
            data = str(data.decode('utf-8', errors='ignore'))
        except BaseException:
            data = "err"
            err_count += 1
        data_in = data.split("__")[0].replace(" ", "\n")
        data_f_p = data.split("__")[1]
        f = open( data_f_p, "r")
        f_str = f.read()
        f_str = f_str.replace("\n", " ")
        sock.send(f_str.encode())
        print("SENDING"+f_str)   
    if "1029876545678" in data:
        sock.close()
        print("Сервер запросил разрыв соединения")
        check_connection = False
    print("______________")




