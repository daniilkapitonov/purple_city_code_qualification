import socket #dla tsp serverov
import sys
import time
from multiprocessing import Process
import multiprocessing
import random
import datetime
import os
import traceback
import random
import os
#Коды для работы с клиентами
#666 - запрос о номере клиента
#102 - завершение работы клиента
#404 - перезагрузка клиента
#167 - подтверждение, что сервер принял режим работы
    

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

def file_update():
    files_name_set()
    print("Процесс обновления файлов запущен.")
    while True:
        f = open (energy_consumption_file, "w")
        f.write("0 \n")
        f.close()
        time.sleep(2)

def files_name_set():
    global adm_house_file
    global batary_file
    global hospital_house_file
    global water_file
    global energy_generate_file
    global house_1_file
    global house_2_file
    global house_all_file
    global buildings_all_file
    global mchs_file 
    global energy_consumption_file 
    global ges_state_file
    global output_file 
    global pred_file 

    global adm_rele_file
    global hospital_rele_file
    global house_1_rele_file
    global house_2_rele_file
    global mchs_rele_file
    global ges_rele_file

    global car_move_file
    os.chdir("Server/Server_files")
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
                    print("Я нашёл файл - ", file, ". По пути - ", os.path.abspath(root1+"/"+file))
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
                    if file in car_move_file:
                        car_move_file = os.path.abspath(root1+"/"+file)
                    i+=1
    if i != len(file_list):
        print ("ERROR Кол-во файлов в массиве и директории", os.getcwd()," не совпадает")

def ard_house_1_2(connection):
    #плита - 0,3 кв
    #духовка - 0,3 кв
    #холодильник - 0,2 кв
    #морозильник - - 0,3 кв
    #общий свет - 0,1 кв
    #прикраватный светильник - 0,05 кв
    #джакузи - 0,1 кв
    # телевизор - 0,1 кв
    check_connection = True
    err_count = 0
    str_print = ""
    try:
        while check_connection:
            f = open(house_all_file, "w")
            f.write("1"+"\n"+"1"+"\n")
            f.close()
            f = open(house_1_rele_file, "r")
            h_1 = f.read().split("\n")
            f.close()
            str_print += f"Дом 1: реле - {h_1}, "
            h_1= h_1[:-1]
            try:
                house_1_energy_con = int(h_1[0])*30 + int(h_1[1])*30 + int(h_1[2])*20 + int(h_1[3])*30 + int(h_1[4])*10 + int(h_1[5])*5 + int(h_1[6])*10 
                house_1_energy_con = round(float(house_1_energy_con)/100, 3)
            except:
                house_1_energy_con = 0
            f_b = open (energy_consumption_file, "r")
            f_b_per = open (batary_file, "r")
            batary_per = str(f_b_per.read()).replace("\n","")
            f_b_per.close()
            batary_con = float(f_b.read().split("\n")[0])
            batary_con += house_1_energy_con
            str_print += f"потребление - {house_1_energy_con}. "
            f_w = open (water_file, "r")
            f = open(house_1_file, "w")
            f.write("1"+"\n"+batary_per+"\n"+f_w.read().split("\n")[0]+"\n"+str(house_1_energy_con)+"\n")
            f.close()
            f_b.close()
            f_b = open (energy_consumption_file, "w")
            f_b.write(str(batary_con)[:5]+"\n")
            f_b.close()
            f_w.close()

            f = open(house_2_rele_file, "r")
            h_2 = f.read().split("\n")
            f.close()
            h_2= h_2[:-1]
            str_print += f"Дом 2: реле - {h_2}, "
            f_b = open (energy_consumption_file, "r")
            f_w = open (water_file, "r")
            try:
                house_2_energy_con = int(h_2[0])*30 + int(h_2[1])*30 + int(h_2[2])*20 + int(h_2[3])*30 + int(h_2[4])*10 + int(h_2[5])*5 + int(h_2[6])*10# + int(h_2[7])*10 
                house_2_energy_con = round(float(house_2_energy_con)/100, 3)
            except:
                house_2_energy_con = 0
            str_print += f"потребление - {house_2_energy_con}. "
            f = open(house_2_file, "w")
            batary_con = float(f_b.read().split("\n")[0])
            batary_con += house_2_energy_con
            f.write("1"+"\n"+batary_per+"\n"+f_w.read().split("\n")[0]+"\n"+str(house_2_energy_con)+"\n")
            f.close()
            f_b.close()
            
            f_b = open (energy_consumption_file, "w")
            f_b.write(str(batary_con)[:5]+"\n")
            f_b.close()
            f_w.close()
            

            
            try:
                connection.send(str("".join(h_1)+"".join(h_2)).encode())
                str_print += " Данные отправлены."
            except BaseException:
                check_connection = False
                f = open(house_all_file, "w")
                f.write("0"+"\n"+"0"+"\n")
                f.close()
                f = open(house_1_file, "w")
                f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
                f.close()
                f = open(house_2_file, "w")
                f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
                f.close()
                str_print += " Разрыва соеднинения."
                print(str_print)
                return
            connection.settimeout(3)
            try:
                data = connection.recv(64)
                data = str(data.decode('utf-8', errors='ignore'))
                data = data.split("_")[0]
                str_print += " Данные получены."
            except BaseException:
                data = "err"
                err_count +=1
                str_print += " Данные не получены."
            if data != "ok":
                err_count+=1
                if err_count > 4:
                    check_connection = False
                    f = open(house_all_file, "w")
                    f.write("0"+"\n"+"0"+"\n")
                    f.close()
                    f = open(house_1_file, "w")
                    f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
                    f.close()
                    f = open(house_2_file, "w")
                    f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
                    f.close()
                    str_print += " Разрыва соеднинения."
                    print(str_print)
                    return "102"
            print (str_print)
            print ()
            str_print = ""
            time.sleep(1.5)    
    except BaseException:
        print("ERROR "+ traceback.format_exc())
        return

def ard_mchs_docum_hospital(connection):
    #МЧС ТВ - 0.1 кв
    #МЧС душ - 0.05 кв
    #МЧС общий свет - 0.2 кв
    #МЧС зарядка для машин - 2 кв
    #МЧС ворота - 0.7 кв
    #АДМ лампы - 0.2 кв
    #АДМ компы - 1.2 кв
    #АДМ рамка - 0.3 кв
    #АДМ табло - 0.1 кв
    #Болиница общий свет - 0.3 кв
    #Болиница кабинет - 1 кв
    check_connection = True
    err_count = 0
    str_print = ""
    try: 
        while check_connection:
            f = open(buildings_all_file, "w")
            f.write("1"+"\n"+"1"+"\n"+"1"+"\n")
            f.close()

            f = open(mchs_rele_file, "r")
            h_1 = f.read().split("\n")
            f.close()
            h_1= h_1[:-1]
            str_print += f"МЧС: реле - {h_1}, "
            try:
                mchs_energy_con = int(h_1[0])*10 + int(h_1[1])*5 + int(h_1[2])*20 + int(h_1[3])*200 + int(h_1[4])*70 
                mchs_energy_con = round(float(mchs_energy_con)/100, 3)
            except:
                mchs_energy_con = 0
            f_b = open (energy_consumption_file, "r")
            f_b_per = open (batary_file, "r")
            batary_per = str(f_b_per.read()).replace("\n","")
            f_b_per.close()
            try:
                batary_con = float(f_b.read().split("\n")[0])
            except BaseException:
                print(f_b.read())
                connection.close()
            batary_con += mchs_energy_con
            str_print += f"потребление - {mchs_energy_con}. "
            f_w = open (water_file, "r")
            f = open(mchs_file, "w")
            f.write("1"+"\n"+batary_per+"\n"+f_w.read().split("\n")[0]+"\n"+str(mchs_energy_con)+"\n")
            f.close()
            f_b.close()
            f_b = open (energy_consumption_file, "w")
            f_b.write(str(batary_con)[:5]+"\n")
            f_b.close()
            f_w.close()

            f = open(adm_rele_file, "r")
            h_2 = f.read().split("\n")
            f.close()
            h_2= h_2[:-1]
            str_print += f"Администрация: реле - {h_2}, "
            f_b = open (energy_consumption_file, "r")
            f_w = open (water_file, "r")
            try:
                adm_energy_con = int(h_2[0])*20 + int(h_2[1])*120 + int(h_2[2])*30 + int(h_2[3])*10 
                adm_energy_con = round(float(adm_energy_con)/100, 3)
            except:
                adm_energy_con = 0
            str_print += f"потребление - {adm_energy_con}. "
            f = open(adm_house_file, "w")
            
            try:
                batary_con = float(f_b.read().split("\n")[0])
            except BaseException:
                print(f_b.read())
                connection.close()
            batary_con += adm_energy_con
            f.write("1"+"\n"+batary_per+"\n"+f_w.read().split("\n")[0]+"\n"+str(adm_energy_con)+"\n")
            f.close()
            f_b.close()

            f = open(hospital_rele_file, "r")
            h_3 = f.read().split("\n")
            f.close()
            h_3= h_3[:-1]
            str_print += f"Больница: реле - {h_3}, "
            f_b = open (energy_consumption_file, "r")
            f_w = open (water_file, "r")
            try:
                adm_energy_con = int(h_3[0])*20 + int(h_3[1])*120 + int(h_3[2])*30 + int(h_3[3])*10 
                adm_energy_con = round(float(adm_energy_con)/100, 3)
            except:
                adm_energy_con = 0
            str_print += f"потребление - {adm_energy_con}. "
            f = open(hospital_house_file, "w")
            
            try:
                batary_con = float(f_b.read().split("\n")[0])
            except BaseException:
                print(f_b.read())
                connection.close()
            batary_con += adm_energy_con
            f.write("1"+"\n"+batary_per+"\n"+f_w.read().split("\n")[0]+"\n"+str(adm_energy_con)+"\n")
            f.close()
            f_b.close()

            f_b = open (energy_consumption_file, "w")
            f_b.write(str(batary_con)[:8]+"\n")
            f_b.close()
            f_w.close()
            
            
            try:
                connection.send(str("".join(h_1)+"".join(h_2)+"".join(h_3)).encode())
                str_print += " Данные отправлены."
            except BaseException:
                check_connection = False
                f = open(buildings_all_file, "w")
                f.write("0"+"\n"+"0"+"\n"+"0"+"\n")
                f.close()
                f = open(mchs_file, "w")
                f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
                f.close()
                f = open(hospital_house_file, "w")
                f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
                f.close()
                f = open(adm_house_file, "w")
                f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
                f.close()
                str_print += " Разрыва соеднинения."
                print(str_print)
                return
            connection.settimeout(3)
            try:
                data = connection.recv(64)
                data = str(data.decode('utf-8', errors='ignore'))
                data = data.split("_")[0]
                str_print += " Данные получены."
            except BaseException:
                data = "err"
                err_count +=1
                str_print += " Данные не получены."
            if data != "ok":
                err_count+=1
                if err_count > 4:
                    check_connection = False
                    f = open(buildings_all_file, "w")
                    f.write("0"+"\n"+"0"+"\n"+"0"+"\n")
                    f.close()
                    f = open(mchs_file, "w")
                    f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
                    f.close()
                    f = open(hospital_house_file, "w")
                    f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
                    f.close()
                    f = open(adm_house_file, "w")
                    f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
                    f.close()
                    str_print += " Разрыва соеднинения."
                    print(str_print)
                    return "102"
            print (str_print)
            str_print = ""
            print ("")
            time.sleep(1.5)
    except BaseException:
        print("ERROR "+ traceback.format_exc())
        return        

def ard_energy_station(connection):
    check_connection = True
    err_count = 0
    try:
        while check_connection:
            f = open (car_move_file, "r")
            move_c = f.read()
            f.close()
            if int(move_c) > 0:
                f = open(car_move_file, "w")
                f.write("000")
                f.close()
                connection.send((move_c+"_").encode())
            else:
                connection.send("999_".encode())
            connection.settimeout(5)
            try:
                data = connection.recv(64)
                data = str(data.decode('utf-8', errors='ignore'))
            except BaseException:
                data = "err"
                err_count =+1
            connection.settimeout(5)
            try:
                data = connection.recv(64)
                data = str(data.decode('utf-8', errors='ignore'))
                data = data.split("_")[0]
            except BaseException:
                data = "err"
                err_count =+1
            print (data)
            data = data.split("+")
            try:
                print ("Потребление 1 - "+data[0]+", потребление 2 - "+data[1]+", выработка ватт - "+data[2])
                f =  open(energy_generate_file, "w")
                f.write(str(data[0])+"\n")

                f.close()
            except BaseException:
                f =  open(energy_generate_file, "w")
                f.write("0"+"\n")
                f.close()
            #connection.send("222".encode())
            f_e_c = open(energy_consumption_file , "r")
            f_pred = open(pred_file, "w")
            f_pred.write(str(random.randint(0,500))+"\n"+f_e_c.read().replace("\n","")+"\n"+str(data[0])+"\n")
            f_pred.close()
            f_e_c.close()
            time.sleep(0.5)
        connection.close()
        return
    except BaseException:
        print("ERROR "+ traceback.format_exc())
        return 

def macbook(connection):
    check_connection = True
    err_count =0 
    i=0
    data = ""
    str_print =""
    try:
        while check_connection:
            for root, dirs, files in os.walk(r"/home/pi/Desktop/RRO/Server/Server_files"):
                for f_name in files:
                    if not ".DS" in f_name:
                        if not "Данные" in root:
                            connection.send("sendyou".encode())
                            connection.settimeout(4)
                            try:
                                data = connection.recv(64)
                            except BaseException:
                                data = "err" 
                                #err_count =+1
                            #print("Отправляющий")
                            f_name = root +r"/" + f_name
                            f = open(f_name, "r")
                            f_str = f.read()
                            #print(f_str)
                            f_str = f_str.replace("\n", " ")                 
                            #connection.send(f_str.encode())
                            f.close()
                            f_name = f_name.replace("/home/pi/Desktop/RRO/Server/Server_files", ".")
                            #print(f_name)
                            f_str += "__"+f_name
                            #print(f_str)
                            connection.send(f_str.encode())
                            connection.settimeout(4)
                            try:
                                data = connection.recv(64)
                            except BaseException:
                                data = "err" 
                                #err_count =+1
                            
                            #print("___________________")
                        else:
                            connection.send("sendme".encode())
                            #print("Принимающий")
                            connection.settimeout(4)
                            try:
                                data = connection.recv(64)
                            except BaseException:
                                data = "err" 
                                #err_count =+1
                            f_name = root +r"/" + f_name
                            f = open(f_name, "r")
                            f_str = f.read()
                            #print(f_str)
                            f_str = f_str.replace("\n", " ")                 
                            #connection.send(f_str.encode())
                            f.close()
                            f_name_cash = f_name
                            f_name = f_name.replace("/home/pi/Desktop/RRO/Server/Server_files", ".")
                            #print(f_name)
                            f_str += "__"+f_name
                            #print(f_str)
                            connection.send(f_str.encode())
                            connection.settimeout(4)
                            try:
                                data = connection.recv(64)
                                data = str(data.decode('utf-8', errors='ignore'))
                            except BaseException:
                                #data = "err"
                                err_count =+1



                                
                            data_in = data.replace(" ", "\n")
                            f_name = f_name_cash
                            if ("move_comand.txt" in f_name):
                                f_c = open(car_move_file, "r")
                                if (int(f_c.read()) == 0   ):
                                    f_c.close()
                                    f = open(f_name, "w")
                                    f.write(data_in)
                                    f.close()
                                f_c.close()
                            else:
                                f = open(f_name, "w")
                                f.write(data_in)
                                f.close()
                            
                            
                        time.sleep(0.05)
            print("Данные на MAC отправлены и получены. ")
            f = open(energy_consumption_file, "r")
            if float(f.read().split("\n")[0]) != 0:
                f.close()
                #f = open(energy_consumption_file, "w")
                #f.write("0")
                #f.close()
            f.close()

            
            connection.settimeout(4)
            # try:
            #     data = connection.recv(64)
            #     data = str(data.decode('utf-8', errors='ignore'))
            # except BaseException:
            #     data = "err"
            #     err_count +=1
            if err_count > 4:
                connection.close()
                print("Клиент macbook не отвечал и был отключён")
            #else:
                #print(data)
            time.sleep(0.2)
            #os.system("clear   ")
        return
    except BaseException:
        print("ERROR "+ traceback.format_exc())
        return 

def ard_ges(connection):
    check_connection = True
    err_count = 0
    str_print = ""
    try:
        while check_connection:
            f = open(ges_state_file, "w")
            f.write("1")
            f.close()
            f = open(ges_rele_file, "r")
            ges = f.read().split("\n")
            f.close()
            str_print += f"ГЭС: реле - {ges}, "
            if int(ges[0])==1:
                f = open(energy_generate_file, "r")
                cash = float(f.read().split("\n")[0])
                f.close()
                if int(cash)<799:
                    cash+=852
                    f = open(energy_generate_file, "w")
                    f.write(str(cash)+"\n")
                    f.close()
            else:
                f = open(energy_generate_file, "r")
                cash = float(f.read().split("\n")[0])
                f.close()
                if int(cash)>799:
                    cash-=852
                    f = open(energy_generate_file, "w")
                    f.write(str(cash)+"\n")
                    f.close()
            try:
                connection.send(str("".join(ges)).encode())
                str_print += " Данные отправлены."
            except BaseException:
                check_connection = False
                
                return
            connection.settimeout(3)
            try:
                data = connection.recv(64)
                data = str(data.decode('utf-8', errors='ignore'))
                data = data.split("_")[0]
                str_print += " Данные получены." + data 
            except BaseException:
                data = "err"
                err_count +=1
                str_print += " Данные не получены."
            if data != "ok":
                err_count+=1
                if err_count > 4:
                    check_connection = False
                    f = open(ges_state_file, "w")
                    f.write("0")
                    f.close()
                    str_print += " Разрыва соеднинения."
                    print(str_print)
                    return "102"
            print (str_print)
            print ()
            str_print = ""
            time.sleep(1.5)    
    except BaseException:
        print("ERROR "+ traceback.format_exc())
        return

def new_client(conection_count, connection, client_address):
    files_name_set()
    num_of_con = conection_count.value
    str_print = ""
    err=0
    str_print +=f"Номер соединения - {num_of_con}" + ' '
    identification = False
    while not identification:
        connection.send("666_".encode())
        connection.settimeout(3)
        try:
            data = connection.recv(128)
            data = str(data.decode('utf-8', errors='ignore'))
            data = data.split("_")[0]
        except BaseException:
            data = "err"
            err_count =+1
        if data == "err" and err_count > 3:
            str_print += "Устрйоство не ответило. Завершение соединения с ним."
            connection.close()
            conection_count.value -= 1
            return
        else:
            identification = True
    str_print += "Устройство подключено. Запрос режима работы - " + data+". "
    work_type = data 
    if data == "house":
        connection.send("167".encode())
        str_print+= "Устройство начинает работу."
        print(str_print)
        ard_house_1_2(connection)
        print("Устройство Arduino House - завершает работу.")        
        f = open(house_all_file, "w")
        f.write("0"+"\n"+"0"+"\n")
        f.close()
        f = open(house_1_file, "w")
        f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
        f.close()
        f = open(house_2_file, "w")
        f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
        f.close()
    elif data == "mchsdochospital":
        connection.send("167".encode())
        str_print+= "Устройство начинает работу."
        print(str_print)
        ard_mchs_docum_hospital(connection)
        print("Устройство Arduino MchsDocHos - завершает работу.")    
        f = open(buildings_all_file, "w")
        f.write("0"+"\n"+"0"+"\n"+"0"+"\n")
        f.close()
        f = open(mchs_file, "w")
        f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
        f.close()
        f = open(hospital_house_file, "w")
        f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
        f.close()
        f = open(adm_house_file, "w")
        f.write("0"+"\n"+"0"+"\n"+"0"+"\n"+"0"+"\n")
        f.close()
    elif data == "energycar":
        connection.send("167".encode())
        str_print+= "Устройство начинает работу."
        print(str_print)
        ard_energy_station(connection)
        print("Устройство Arduino Energy, car remote - завершает работу.")    
    elif data == "macbook":
        connection.send("167".encode())
        str_print+= "Устройство начинает работу."
        print(str_print)
        macbook(connection)
        print("Устройство MacBook - завершает работу.")   
    elif data == "ges":
        connection.send("167".encode())
        str_print+= "Устройство начинает работу."
        print(str_print)
        ard_ges(connection)
        print("Устройство Ges - завершает работу.")
        f = open(ges_state_file, "w")
        f.write("0")
        f.close()   
    else:
        str_print+= "Режим работы отсуствует. Отключение"
        connection.send("102".encode())
        connection.close()
    str_print += f"Завершение работы клиента {work_type} под номеров {num_of_con} с сервером. "    
    conection_count.value -=1
    print(str_print)
    print()

if __name__ == '__main__':
    
   
    f = open(buildings_all_file, "w")
    f.write("0"+"\n"+"0"+"\n"+"0"+"\n")
    f.close()
    f = open(house_all_file, "w")
    f.write("0"+"\n"+"0"+"\n")
    f.close()
    # создаемTCP/IP сокет
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Привязываем сокет к порту
    proc = []
    conection_count = multiprocessing.Value('i', 1)
    new_proc = Process(target = file_update)
    proc.append(new_proc)
    new_proc.start()
    time.sleep(1)
    try:
        server_address = ('0.0.0.0', 10000)
        print('Старт сервера на {} порт {}'.format(*server_address))
        sock.bind(server_address)
    except BaseException:
        server_address = ('0.0.0.0', 10001)
        print('Старт сервера на {} порт {}'.format(*server_address))
        sock.bind(server_address)
    sock.listen(10)

    
    while True:
        print('Ожидание соединения...')
        connection, client_address = sock.accept()
        print('Подключено к:', client_address)
        # Принимаем данные порциями и ретранслируем их
        new_proc = Process(target = new_client, args = (conection_count, connection, client_address))
        proc.append(new_proc)
        new_proc.start()
        time.sleep(1)
        conection_count.value += 1
