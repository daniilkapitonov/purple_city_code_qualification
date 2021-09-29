import builtins
import tkinter
from tkinter import *
import os
import time
from tkinter import font
from tkinter.font import BOLD

def click_btn_adm_metald():
    value = rele_file_read_edit(0, adm_rele_file,0)
    if value == 0:
        lbl_adm_metald_status.configure(text= "- выключено")
    else:
        lbl_adm_metald_status.configure(text= "- включено")
    btn_click_analyze(3,value)

def click_btn_adm_pc():
    value = rele_file_read_edit(0, adm_rele_file,1)
    if value == 0:
        lbl_adm_pc_status.configure(text= "- выключено")
    else:
        lbl_adm_pc_status.configure(text= "- включено")
    btn_click_analyze(3,value)

def click_btn_adm_tv():
    value = rele_file_read_edit(0, adm_rele_file,2)
    if value == 0:
        lbl_adm_tv_status.configure(text= "- выключено")
    else:
        lbl_adm_tv_status.configure(text= "- включено")
    btn_click_analyze(3,value)

def click_btn_adm_leds():
    value = rele_file_read_edit(0, adm_rele_file,3)
    if value == 0:
        lbl_adm_leds_status.configure(text= "- выключено")
    else:
        lbl_adm_leds_status.configure(text= "- включено")
    btn_click_analyze(3,value)

def click_btn_house1_cook_plate():
    value = rele_file_read_edit(0, house_1_rele_file,0)
    if value == 0:
        lbl_house1_cook_plate_status.configure(text= "- выключено")
    else:
        lbl_house1_cook_plate_status.configure(text= "- включено")
    btn_click_analyze(1,value)

def click_btn_house1_oven():
    value = rele_file_read_edit(0, house_1_rele_file,1)
    if value == 0:
        lbl_house1_oven_status.configure(text= "- выключено")
    else:
        lbl_house1_oven_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_house1_freez_up():
    value = rele_file_read_edit(0, house_1_rele_file,2)
    if value == 0:
        lbl_house1_freez_up_status.configure(text= "- выключено")
    else:
        lbl_house1_freez_up_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_house1_freez_down():
    value = rele_file_read_edit(0, house_1_rele_file,3)
    if value == 0:
        lbl_house1_freez_down_status.configure(text= "- выключено")
    else:
        lbl_house1_freez_down_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_house1_all_light():
    value = rele_file_read_edit(0, house_1_rele_file,4)
    if value == 0:
        lbl_house1_all_light_status.configure(text= "- выключено")
    else:
        lbl_house1_all_light_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_house1_bed_lamd():
    value = rele_file_read_edit(0, house_1_rele_file,5)
    if value == 0:
        lbl_house1_bed_lamd_status.configure(text= "- выключено")
    else:
        lbl_house1_bed_lamd_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_house1_hot_tub():
    value = rele_file_read_edit(0, house_1_rele_file,6)
    if value == 0:
        lbl_house1_hot_tub_status.configure(text= "- выключено")
    else:
        lbl_house1_hot_tub_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_house2_cook_plate():
    value = rele_file_read_edit(0, house_2_rele_file,0)
    if value == 0:
        lbl_house2_cook_plate_status.configure(text= "- выключено")
    else:
        lbl_house2_cook_plate_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_house2_oven():
    value = rele_file_read_edit(0, house_2_rele_file,1)
    if value == 0:
        lbl_house2_oven_status.configure(text= "- выключено")
    else:
        lbl_house2_oven_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_house2_freez_up():
    value = rele_file_read_edit(0, house_2_rele_file,2)
    if value == 0:
        lbl_house2_freez_up_status.configure(text= "- выключено")
    else:
        lbl_house2_freez_up_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_house2_freez_down():
    value = rele_file_read_edit(0, house_2_rele_file,3)
    if value == 0:
        lbl_house2_freez_down_status.configure(text= "- выключено")
    else:
        lbl_house2_freez_down_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_house2_all_light():
    value = rele_file_read_edit(0, house_2_rele_file,4)
    if value == 0:
        lbl_house2_all_light_status.configure(text= "- выключено")
    else:
        lbl_house2_all_light_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_house2_bed_lamd():
    value = rele_file_read_edit(0, house_2_rele_file,5)
    if value == 0:
        lbl_house2_bed_lamd_status.configure(text= "- выключено")
    else:
        lbl_house2_bed_lamd_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_house2_tv():
    value = rele_file_read_edit(0, house_2_rele_file,6)
    if value == 0:
        lbl_house2_tv_status.configure(text= "- выключено")
    else:
        lbl_house2_tv_status.configure(text= "- включено")
    btn_click_analyze(2,value)

def click_btn_mchs_gates():
    value = rele_file_read_edit(0, mchs_rele_file,0)
    if value == 0:
        lbl_mchs_gates_status.configure(text= "- выключено")
    else:
        lbl_mchs_gates_status.configure(text= "- включено")
    btn_click_analyze(4,value)

def click_btn_mchs_charge():
    value = rele_file_read_edit(0, mchs_rele_file,1)
    if value == 0:
        lbl_mchs_charge_status.configure(text= "- выключено")
    else:
        lbl_mchs_charge_status.configure(text= "- включено")
    btn_click_analyze(4,value)

def click_btn_mchs_all_light():
    value = rele_file_read_edit(0, mchs_rele_file,2)
    if value == 0:
        lbl_mchs_all_light_status.configure(text= "- выключено")
    else:
        lbl_mchs_all_light_status.configure(text= "- включено")
    btn_click_analyze(4,value)

def click_btn_mchs_light_shower():
    value = rele_file_read_edit(0, mchs_rele_file,3)
    if value == 0:
        lbl_mchs_light_shower_status.configure(text= "- выключено")
    else:
        lbl_mchs_light_shower_status.configure(text= "- включено")
    btn_click_analyze(4,value)

def click_btn_mchs_tv():
    value = rele_file_read_edit(0, mchs_rele_file,4)
    if value == 0:
        lbl_mchs_tv_status.configure(text= "- выключено")
    else:
        lbl_mchs_tv_status.configure(text= "- включено")
    btn_click_analyze(4,value)

def click_btn_hospital_all_light():
    value = rele_file_read_edit(0, hospital_rele_file,0)
    if value == 0:
        lbl_hospital_all_light_status.configure(text= "- выключено")
    else:
        lbl_hospital_all_light_status.configure(text= "- включено")
    btn_click_analyze(5,value)

def click_btn_hospital_room_1():
    value = rele_file_read_edit(0, hospital_rele_file,1)
    if value == 0:
        lbl_hospital_room_1_status.configure(text= "- выключено")
    else:
        lbl_hospital_room_1_status.configure(text= "- включено")
    btn_click_analyze(5,value)

def click_btn_hospital_room_2():
    value = rele_file_read_edit(0, hospital_rele_file,2)
    if value == 0:
        lbl_hospital_room_2_status.configure(text= "- выключено")
    else:
        lbl_hospital_room_2_status.configure(text= "- включено")
    btn_click_analyze(5,value)

def click_btn_hospital_room_3():
    value = rele_file_read_edit(0, hospital_rele_file,3)
    if value == 0:
        lbl_hospital_room_3_status.configure(text= "- выключено")
    else:
        lbl_hospital_room_3_status.configure(text= "- включено")
    btn_click_analyze(5,value)

def click_btn_hospital_room_4():
    value = rele_file_read_edit(0, hospital_rele_file,4)
    if value == 0:
        lbl_hospital_room_4_status.configure(text= "- выключено")
    else:
        lbl_hospital_room_4_status.configure(text= "- включено")
    btn_click_analyze(5,value)

def click_btn_ges_water_in():    
    value = rele_file_read_edit(0, ges_rele_file,0)
    f = open(ges_rele_file, "r")
    if f.read().split("\n")[1] != str(value) or str(value)=="0" : 
        if value == 0:
            lbl_ges_water_in_status.configure(text= "- не активно")
        else:
            lbl_ges_water_in_status.configure(text= "- активно")
        btn_click_analyze(0,value)
    else:
        value = rele_file_read_edit(0, ges_rele_file,0)
    f.close()

def click_btn_ges_water_out():
    value = rele_file_read_edit(0, ges_rele_file,1)
    f = open(ges_rele_file, "r")
    if f.read().split("\n")[0] != str(value) or str(value)=="0" : 
        if value == 0:
            lbl_ges_water_out_status.configure(text= "- не активно")
        else:
            lbl_ges_water_out_status.configure(text= "- активно")
        btn_click_analyze(0,value)
    else:
        value = rele_file_read_edit(0, ges_rele_file,1)
    f.close()

def lbl_condition_check():
    f = open(adm_rele_file, "r")
    value = f.read().split("\n")
    f.close()
    if value[0] == "0":
        lbl_adm_metald_status.configure(text= "- выключено")
    else:
        lbl_adm_metald_status.configure(text= "- включено")

    if value[1] == "0":
        lbl_adm_pc_status.configure(text= "- выключено")
    else:
        lbl_adm_pc_status.configure(text= "- включено")

    if value[2] == "0":
        lbl_adm_tv_status.configure(text= "- выключено")
    else:
        lbl_adm_tv_status.configure(text= "- включено")

    if value[3] == "0":
        lbl_adm_leds_status.configure(text= "- выключено")
    else:
        lbl_adm_leds_status.configure(text= "- включено")
    value = []

    f = open(house_1_rele_file, "r")
    value = f.read().split("\n")
    f.close()
    if value[0] == "0":
        lbl_house1_cook_plate_status.configure(text= "- выключено")
    else:
        lbl_house1_cook_plate_status.configure(text= "- включено")

    if value[1] == "0":
        lbl_house1_oven_status.configure(text= "- выключено")
    else:
        lbl_house1_oven_status.configure(text= "- включено")

    if value[2] == "0":
        lbl_house1_freez_up_status.configure(text= "- выключено")
    else:
        lbl_house1_freez_up_status.configure(text= "- включено")

    if value[3] == "0":
        lbl_house1_freez_down_status.configure(text= "- выключено")
    else:
        lbl_house1_freez_down_status.configure(text= "- включено")

    if value[4] == "0":
        lbl_house1_all_light_status.configure(text= "- выключено")
    else:
        lbl_house1_all_light_status.configure(text= "- включено")

    if value[5] == "0":
        lbl_house1_bed_lamd_status.configure(text= "- выключено")
    else:
        lbl_house1_bed_lamd_status.configure(text= "- включено")

    if value[6] == "0":
        lbl_house1_hot_tub_status.configure(text= "- выключено")
    else:
        lbl_house1_hot_tub_status.configure(text= "- включено")
    value = []

    f = open(house_2_rele_file, "r")
    value = f.read().split("\n")
    f.close()
    if value[0] == "0":
        lbl_house2_cook_plate_status.configure(text= "- выключено")
    else:
        lbl_house2_cook_plate_status.configure(text= "- включено")

    if value[1] == "0":
        lbl_house2_oven_status.configure(text= "- выключено")
    else:
        lbl_house2_oven_status.configure(text= "- включено")

    if value[2] == "0":
        lbl_house2_freez_up_status.configure(text= "- выключено")
    else:
        lbl_house2_freez_up_status.configure(text= "- включено")

    if value[3] == "0":
        lbl_house2_freez_down_status.configure(text= "- выключено")
    else:
        lbl_house2_freez_down_status.configure(text= "- включено")

    if value[4] == "0":
        lbl_house2_all_light_status.configure(text= "- выключено")
    else:
        lbl_house2_all_light_status.configure(text= "- включено")

    if value[5] == "0":
        lbl_house2_bed_lamd_status.configure(text= "- выключено")
    else:
        lbl_house2_bed_lamd_status.configure(text= "- включено")

    if value[6] == "0":
        lbl_house2_tv_status.configure(text= "- выключено")
    else:
        lbl_house2_tv_status.configure(text= "- включено")
    value = []

    f = open(mchs_rele_file, "r")
    value = f.read().split("\n")
    f.close()
    if value[0] == "0":
        lbl_mchs_gates_status.configure(text= "- выключено")
    else:
        lbl_mchs_gates_status.configure(text= "- включено")

    if value[1] == "0":
        lbl_mchs_charge_status.configure(text= "- выключено")
    else:
        lbl_mchs_charge_status.configure(text= "- включено")

    if value[2] == "0":
        lbl_mchs_all_light_status.configure(text= "- выключено")
    else:
        lbl_mchs_all_light_status.configure(text= "- включено")

    if value[3] == "0":
        lbl_mchs_light_shower_status.configure(text= "- выключено")
    else:
        lbl_mchs_light_shower_status.configure(text= "- включено")

    if value[4] == "0":
        lbl_mchs_tv_status.configure(text= "- выключено")
    else:
        lbl_mchs_tv_status.configure(text= "- включено")
    value = []

    f = open(hospital_rele_file, "r")
    value = f.read().split("\n")
    f.close()
    if value[0] == "0":
        lbl_hospital_all_light_status.configure(text= "- выключено")
    else:
        lbl_hospital_all_light_status.configure(text= "- включено")

    if value[1] == "0":
        lbl_hospital_room_1_status.configure(text= "- выключено")
    else:
        lbl_hospital_room_1_status.configure(text= "- включено")

    if value[2] == "0":
        lbl_hospital_room_2_status.configure(text= "- выключено")
    else:
        lbl_hospital_room_2_status.configure(text= "- включено")

    if value[3] == "0":
        lbl_hospital_room_3_status.configure(text= "- выключено")
    else:
        lbl_hospital_room_3_status.configure(text= "- включено")

    if value[4] == "0":
        lbl_hospital_room_4_status.configure(text= "- выключено")
    else:
        lbl_hospital_room_4_status.configure(text= "- включено")
    value = []
    
    f = open(ges_rele_file, "r")
    value = f.read().split("\n")
    f.close()
    if value[0] == "0":
        lbl_ges_water_in_status.configure(text= "- не активно")
    else:
        lbl_ges_water_in_status.configure(text= "- активно")

    if value[1] == "0":
        lbl_ges_water_out_status.configure(text= "- не активно")
    else:
        lbl_ges_water_out_status.configure(text= "- активно")
    value = []

    
def rele_file_read_edit(work_type, file_path, bit_number):
    f = open (file_path, "r")
    rele = f.read().split("\n")
    f.close()
    f = open (file_path, "w")
    if work_type == 0:
        if rele[bit_number] == "0":
            rele[bit_number] = "1"
            cash = 1
        else:
            rele[bit_number] = "0"
            cash = 0
        
    elif work_type == 1:
        rele[bit_number] = "0"
        cash = 0
    elif work_type == 2:
        rele[bit_number] = "1"
        cash = 1
    f.write("\n".join(rele))
    f.close()
    return cash

def btn_click_analyze(building_num, led_num):
    if building_num == 0:
        print("Работа с реле на ГЭС")
        if led_num == 0:
            print("Выключение устройства")
        else:
            print("Включение устройства")
    if building_num == 1:
        print("Работа с реле в Дом №1")
        if led_num == 0:
            print("Выключение устройства")
        else:
            print("Включение устройства")
    if building_num == 2:
        print("Работа с реле в Дом №2")
        if led_num == 0:
            print("Выключение устройства")
        else:
            print("Включение устройства")
    if building_num == 3:
        print("Работа с реле в администрации")
        if led_num == 0:
            print("Выключение устройства")
        else:
            print("Включение устройства")
    if building_num == 4:
        print("Работа с реле в МЧС")
        if led_num == 0:
            print("Выключение устройства")
        else:
            print("Включение устройства")
    if building_num == 5:
        print("Работа с реле в больнице")
        if led_num == 0:
            print("Выключение устройства")
        else:
            print("Включение устройства")

def all_off():
    f = open(adm_rele_file, "w")
    f.write("0\n0\n0\n0\n")
    f.close()

    f = open(mchs_rele_file, "w")
    f.write("0\n0\n0\n0\n0\n")
    f.close()

    f = open(hospital_rele_file, "w")
    f.write("0\n0\n0\n0\n0\n")
    f.close()

    f = open(house_1_rele_file, "w")
    f.write("0\n0\n0\n0\n0\n0\n0\n")
    f.close()

    f = open(house_2_rele_file, "w")
    f.write("0\n0\n0\n0\n0\n0\n0\n")
    f.close()

    f = open(ges_rele_file, "w")
    f.write("0\n0\n")
    f.close()

    lbl_condition_check()

def all_on():
    f = open(adm_rele_file, "w")
    f.write("1\n1\n1\n1\n")
    f.close()

    f = open(mchs_rele_file, "w")
    f.write("1\n1\n1\n1\n1\n")
    f.close()

    f = open(hospital_rele_file, "w")
    f.write("1\n1\n1\n1\n1\n")
    f.close()

    f = open(house_1_rele_file, "w")
    f.write("1\n1\n1\n1\n1\n1\n1\n")
    f.close()

    f = open(house_2_rele_file, "w")
    f.write("1\n1\n1\n1\n1\n1\n1\n")
    f.close()

    lbl_condition_check()

def work_type():
    global worktype
    if worktype:
        worktype = False
    else:
        worktype = True
    info_update()

def info_update():
    global worktype
    if worktype:
        f = open(batary_file, "r")
        cash = int(f.read().split("\n")[0])
        lbl_cur_work_type.configure(fg= "black")
        if cash < 20:
            lbl_cur_work_type.configure(text= "Режим энергосбережения")
        if cash in range(20,50):
            lbl_cur_work_type.configure(text= "Режим сохранения энергии")
        if cash in range(50,80):
            lbl_cur_work_type.configure(text= "Стандартный режим")
        if cash >= 80:
            lbl_cur_work_type.configure(text= "Режим переработки")
        perms_set(cash)
        f.close()
    else:
        lbl_cur_work_type.configure(text= "Ручной режим работы", fg = "blue")
        perms_set(101)

    f = open(energy_consumption_file, "r")
    cash = float(f.read().split("\n")[0])
    lbl_energy_spend.configure(text=f"Энергии тратится: {cash} ампер")
    f.close()

    f = open(energy_generate_file, "r")
    cash = int(f.read().split("\n")[0])
    lbl_energy_generate.configure(text = f"Энергии вырабатывается:\n{cash} ампер")
    f.close()

    f = open(water_file, "r")
    cash = int(f.read().split("\n")[0])
    lbl_water_in_ges.configure(text = f"Воды в ГЭС: {cash} литров")
    f.close()

    f = open(batary_file,"r")
    cash = int(f.read().split("\n")[0])
    lbl_batary_per.configure(text = f"Заряд батарей: {cash}%")
    f.close()

    f = open(hospital_house_file, "r")
    cash = int(f.read().split("\n")[0])
    if cash == 1:
        lbl_hospital_status.configure(text="Подключено", fg="green")
    else:
        lbl_hospital_status.configure(text="Отключено", fg="red")
    f.close()

    f = open(mchs_file, "r")
    cash = int(f.read().split("\n")[0])
    if cash == 1:
        lbl_mchs_status.configure(text="Подключено", fg="green")
    else:
        lbl_mchs_status.configure(text="Отключено", fg="red")
    f.close()

    f = open(house_1_file, "r")
    cash = int(f.read().split("\n")[0])
    if cash == 1:
        lbl_house1_status.configure(text="Подключено", fg="green")
    else:
        lbl_house1_status.configure(text="Отключено", fg="red")
    f.close()

    f = open(house_2_file, "r")
    cash = int(f.read().split("\n")[0])
    if cash == 1:
        lbl_house2_status.configure(text="Подключено", fg="green")
    else:
        lbl_house2_status.configure(text="Отключено", fg="red")
    f.close()

    f = open(adm_house_file, "r")
    cash = int(f.read().split("\n")[0])
    if cash == 1:
        lbl_adm_status.configure(text="Подключено", fg="green")
    else:
        lbl_adm_status.configure(text="Отключено", fg="red")
    f.close()

    f = open(ges_state_file, "r")
    cash = int(f.read().split("\n")[0])
    if cash == 1:
        lbl_ges_status.configure(text="Подключено", fg="green")
    else:
        lbl_ges_status.configure(text="Отключено", fg="red")
    f.close()



    
    print("Обновление удачно")
    window.after(2000, info_update)

def perms_set(value):
    global buttons_mass
    for button in buttons_mass:
        button.configure(state = "normal")
    if value in range(50,80):
        rele_file_read_edit(1, ges_rele_file, 0)
        rele_file_read_edit(1, ges_rele_file, 1)
        lbl_condition_check()
    if value in range(80,100):
        rele_file_read_edit(2, mchs_rele_file, 1)
        rele_file_read_edit(2, house_1_rele_file, 1)
        rele_file_read_edit(2, house_2_rele_file, 1)
        rele_file_read_edit(2, ges_rele_file, 0)
        rele_file_read_edit(1, ges_rele_file, 1)
        lbl_condition_check()
    if value in range(20,49):
        rele_file_read_edit(1, house_1_rele_file, 5)
        rele_file_read_edit(1, house_1_rele_file, 6)
        rele_file_read_edit(1, house_2_rele_file, 5)
        rele_file_read_edit(1, house_2_rele_file, 6)
        rele_file_read_edit(1, adm_rele_file, 2)
        rele_file_read_edit(1, ges_rele_file, 0)
        rele_file_read_edit(1, ges_rele_file, 1)
        btn_house1_bed_lamd.configure(state = "disable")
        btn_house1_hot_tub.configure(state= "disable")
        btn_house2_bed_lamd.configure(state = "disable")
        btn_house2_tv.configure(state= "disable")
        btn_adm_tv.configure(state= "disable")
        
        lbl_condition_check()
    if value <=20:
        rele_file_read_edit(1, house_1_rele_file, 5)
        rele_file_read_edit(1, house_1_rele_file, 6)
        rele_file_read_edit(1, house_1_rele_file,0)
        rele_file_read_edit(1, house_1_rele_file,1)
        rele_file_read_edit(1, house_2_rele_file, 5)
        rele_file_read_edit(1, house_2_rele_file, 6)
        rele_file_read_edit(1, house_2_rele_file,0)
        rele_file_read_edit(1, house_2_rele_file,1)
        rele_file_read_edit(1, adm_rele_file, 2)
        rele_file_read_edit(1, adm_rele_file,0)
        rele_file_read_edit(1, mchs_rele_file, 3)
        rele_file_read_edit(1, mchs_rele_file, 4)
        rele_file_read_edit(2, ges_rele_file, 1)
        rele_file_read_edit(1, ges_rele_file, 0)
        btn_house1_bed_lamd.configure(state = "disable")
        btn_house1_hot_tub.configure(state= "disable")
        btn_house1_cook_plate.configure(state = "disable")
        btn_house1_oven.configure(state = "disable")
        btn_house2_bed_lamd.configure(state = "disable")
        btn_house2_tv.configure(state= "disable")
        btn_house2_cook_plate.configure(state = "disable")
        btn_house2_oven.configure(state = "disable")
        btn_adm_metald.configure(state="disable")
        btn_adm_tv.configure(state= "disable")
        btn_mchs_light_shower.configure(state = "disable")
        btn_mchs_tv.configure(state = "disable")
        lbl_condition_check()


def exit_pr():
    window.quit()

def click_btn_start_car_control():
    window_car_control = Tk()
    window_car_control.title("ДУ")

    global btn_car_w
    global btn_car_a
    global btn_car_s
    global btn_car_d

    btn_car_w = Button(window_car_control, text= "W", font = main_txt_font, command=click_btn_car_w, height = 5, width=5, activeforeground = "red")
    btn_car_w.grid(column = 1, row = 0)

    btn_car_a = Button(window_car_control, text= "A", font = main_txt_font, command=click_btn_car_a, height = 5, width=5, activeforeground = "red")
    btn_car_a.grid(column = 0, row = 1)

    btn_car_s = Button(window_car_control, text= "S", font = main_txt_font, command=click_btn_car_s, height = 5, width=5, activeforeground = "red")
    btn_car_s.grid(column = 1, row = 1)

    btn_car_d = Button(window_car_control, text= "D", font = main_txt_font, command=click_btn_car_d, height = 5, width=5, activeforeground = "red")
    btn_car_d.grid(column = 2, row = 1)
    window_car_control.mainloop()

    

def click_btn_car_w():
    btn_car_w.sta
    i=0

def click_btn_car_a():
    i=0

def click_btn_car_s():
    i=0

def click_btn_car_d():
    i=0

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
def_txt_font = ("Arial Bold", 14)
main_txt_font = ("Arial Bold", 14, "bold")

worktype = True

window = Tk()
window.title("Личный кабинет города Purple City")

for i in range (0, 20):
    pad_px = 8
    window.rowconfigure (i, pad=pad_px)
    window.columnconfigure(i, pad= pad_px)

buttons = []
#Зона информации
lbl_cur_work_type = Label(window, text="Стандартный режим работы", font = main_txt_font)
lbl_cur_work_type.grid(column=0, row=0, columnspan=2)

lbl_energy_spend = Label(window, text = "Энергии тратится: 0 ампер", font = def_txt_font)
lbl_energy_spend.grid(column= 0 , row= 1, columnspan=2)

lbl_energy_generate = Label(window, text= "Энергии вырабатывается:\n0 ампер", font = def_txt_font)
lbl_energy_generate.grid(column=0, row= 2, columnspan=2)

lbl_water_in_ges = Label(window, text= "Воды в ГЭС: 0 литров", font= def_txt_font)
lbl_water_in_ges.grid(column=0,row=3, columnspan=2)

lbl_batary_per = Label(window, text="Заряд батарей: 0%", font= def_txt_font)
lbl_batary_per.grid(column=0, row=4, columnspan=2)

#Зона ГЭС
lbl_ges_title = Label(window, text="ГЭС", font= main_txt_font)
lbl_ges_title.grid(column=0, columnspan=2,row=5)

lbl_ges_status = Label(window, text="Отключено", font = main_txt_font, fg = "red")
lbl_ges_status.grid(columnspan=2, column=0, row=6)

btn_ges_water_in = Button(window, text="Закачать воду", font= def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_ges_water_in)
btn_ges_water_in.grid(column=0, row=7)

lbl_ges_water_in_status = Label(window, text="- не активно", font= def_txt_font)
lbl_ges_water_in_status.grid(column=1, row=7)

btn_ges_water_out = Button(window, text="Выкачать воду", font= def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_ges_water_out)
btn_ges_water_out.grid(column=0, row=8)

lbl_ges_water_out_status = Label(window, text="- не активно", font= def_txt_font)
lbl_ges_water_out_status.grid(column=1, row=8)
buttons.append([btn_ges_water_in, btn_ges_water_out])
#Зона администрации
lbl_adm_title = Label(window, text="Здание Администрации", font = main_txt_font)
lbl_adm_title.grid(column=0, row=10, columnspan=2)

lbl_adm_status = Label(window, text="Отключено", font=main_txt_font, fg = "red")
lbl_adm_status.grid(column=0 ,row=11,columnspan=2)

lbl_adm_money_val = Label(window, text="Счёт: 0 px", font = def_txt_font)
lbl_adm_money_val.grid(column=0,row=12, columnspan= 2)

btn_adm_metald = Button(window, text="Металлоискатель", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command = click_btn_adm_metald)
btn_adm_metald.grid(column=0,row=13)

lbl_adm_metald_status = Label(window, text="- выключено", font= def_txt_font)
lbl_adm_metald_status.grid(column=1, row=13)

btn_adm_pc = Button(window, text="Компютеры", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_adm_pc)
btn_adm_pc.grid(column=0, row=14)

lbl_adm_pc_status = Label(window,text="- выключено", font=def_txt_font)
lbl_adm_pc_status.grid(column=1, row=14)

btn_adm_tv = Button(window, text="Табло", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_adm_tv)
btn_adm_tv.grid(column=0, row=15)

lbl_adm_tv_status = Label(window, text="- выключено", font=def_txt_font)
lbl_adm_tv_status.grid(column=1, row=15)

btn_adm_leds = Button(window, text="Лампы", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_adm_leds)
btn_adm_leds.grid(column=0,row=16)

lbl_adm_leds_status = Label(window, text="- выключено", font = def_txt_font)
lbl_adm_leds_status.grid(column=1, row=16)
buttons.append([btn_adm_leds, btn_adm_metald, btn_adm_pc, btn_adm_tv])
#Зона МЧС
lbl_mchs_title = Label(window, text="МЧС", font=main_txt_font)
lbl_mchs_title.grid(column=2, row=10, columnspan=2)

lbl_mchs_status = Label(window, text="Отключено", font=main_txt_font, fg ="red")
lbl_mchs_status.grid(columnspan=2, column=2, row=11)

lbl_mchs_money_val = Label(window, text="Счёт: 0 px", font=def_txt_font)
lbl_mchs_money_val.grid(column=2, row=12, columnspan=2)

btn_mchs_gates = Button(window,text="Ворота", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_mchs_gates)
btn_mchs_gates.grid(column = 2, row=13)

lbl_mchs_gates_status = Label(window, text="- выключено", font=def_txt_font)
lbl_mchs_gates_status.grid(column=3, row=13)

btn_mchs_charge = Button(window, text="Зарядка", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_mchs_charge)
btn_mchs_charge.grid(column=2, row=14)

lbl_mchs_charge_status = Label(window, text="- выключено", font=def_txt_font)
lbl_mchs_charge_status.grid(column=3, row=14)

btn_mchs_all_light = Button(window, text="Общий свет", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_mchs_all_light)
btn_mchs_all_light.grid(column=2, row=15)

lbl_mchs_all_light_status = Label(window, text = "- выключено", font=def_txt_font)
lbl_mchs_all_light_status.grid(column=3, row=15)

btn_mchs_light_shower = Button(window, text="Свет в душевой", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_mchs_light_shower)
btn_mchs_light_shower.grid(column=2, row = 16)

lbl_mchs_light_shower_status = Label(window, text="- выключено", font=def_txt_font)
lbl_mchs_light_shower_status.grid(column=3, row=16)

btn_mchs_tv = Button(window, text="Телевизор", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_mchs_tv)
btn_mchs_tv.grid(column=2, row=17)

lbl_mchs_tv_status = Label(window, text="- выключено", font=def_txt_font)
lbl_mchs_tv_status.grid(column=3, row=17)
buttons.append([btn_mchs_all_light, btn_mchs_charge, btn_mchs_gates, btn_mchs_light_shower, btn_mchs_tv])
#Зона Больницы
lbl_hospital_title = Label(window, text="Больница", font=main_txt_font)
lbl_hospital_title.grid(column=4, row=10, columnspan=2)

lbl_hospital_status = Label(window,text="Отключено", font=main_txt_font, fg = "red")
lbl_hospital_status.grid(columnspan=2, column=4, row=11)

lbl_hospital_money_val = Label(window, text = "Счёт: 0 px", font=def_txt_font)
lbl_hospital_money_val.grid(column=4, row=12, columnspan=2)

btn_hospital_all_light = Button(window, text="Общий свет", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_hospital_all_light)
btn_hospital_all_light.grid(column=4, row=13)

lbl_hospital_all_light_status = Label(window, text= "- выключено", font=def_txt_font)
lbl_hospital_all_light_status.grid(column=5, row=13)

btn_hospital_room_1 = Button(window, text="Палата №1",font= def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_hospital_room_1)
btn_hospital_room_1.grid(column=4, row=14)

lbl_hospital_room_1_status = Label(window, text="- выключено", font = def_txt_font)
lbl_hospital_room_1_status.grid(column=5, row=14)

btn_hospital_room_2 = Button(window, text="Палата №2",font= def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_hospital_room_2)
btn_hospital_room_2.grid(column=4, row=15)

lbl_hospital_room_2_status = Label(window, text="- выключено", font = def_txt_font)
lbl_hospital_room_2_status.grid(column=5, row=15)

btn_hospital_room_3 = Button(window, text="Палата №3",font= def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_hospital_room_3)
btn_hospital_room_3.grid(column=4, row=16)

lbl_hospital_room_3_status = Label(window, text="- выключено", font = def_txt_font)
lbl_hospital_room_3_status.grid(column=5, row=16)

btn_hospital_room_4 = Button(window, text="Палата №4",font= def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_hospital_room_4)
#btn_hospital_room_4.grid(column=4, row=17)

lbl_hospital_room_4_status = Label(window, text="- выключено", font = def_txt_font)
#lbl_hospital_room_4_status.grid(column=5, row=17)
buttons.append([btn_hospital_all_light, btn_hospital_room_1, btn_hospital_room_2, btn_hospital_room_3, btn_hospital_room_4])

#Зона Дом №1
lbl_house1_title = Label(window,text="Коттедж №1" , font= main_txt_font)
lbl_house1_title.grid(column=2, row=0, columnspan=2)

lbl_house1_status = Label(window, text="Отключено", font=main_txt_font, fg="red")
lbl_house1_status.grid(column=2, row=1, columnspan=2)

lbl_house1_money_val = Label(window, text="Счёт: 0 px", font=def_txt_font)
lbl_house1_money_val.grid(column=2, row=2,columnspan=2 )

btn_house1_cook_plate = Button(window, text="Плита", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house1_cook_plate)
btn_house1_cook_plate.grid(column=2, row=3)

lbl_house1_cook_plate_status = Label(window, text = "- выключено", font=def_txt_font)
lbl_house1_cook_plate_status.grid(column=3, row=3)

btn_house1_oven = Button(window, text="Духовка", font = def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house1_oven)
btn_house1_oven.grid(column=2, row=4)

lbl_house1_oven_status = Label(window, text="- выключено", font=def_txt_font)
lbl_house1_oven_status.grid(column=3, row=4)

btn_house1_freez_up = Button(window, text="Холодильник", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house1_freez_up)
btn_house1_freez_up.grid(column=2, row=5)

lbl_house1_freez_up_status = Label(window, text="- выключено", font=def_txt_font)
lbl_house1_freez_up_status.grid(column=3, row=5)

btn_house1_freez_down = Button(window, text="Морозильник", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house1_freez_down)
btn_house1_freez_down.grid(column=2, row=6)

lbl_house1_freez_down_status = Label(window, text="- выключено", font=def_txt_font)
lbl_house1_freez_down_status.grid(column=3, row=6)

btn_house1_all_light = Button(window, text="Общий свет", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house1_all_light)
btn_house1_all_light.grid(column=2, row=7)

lbl_house1_all_light_status = Label(window, text="- выключено", font=def_txt_font)
lbl_house1_all_light_status.grid(column=3, row=7)

btn_house1_bed_lamd = Button(window, text="Прикроватные лампы", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house1_bed_lamd)
btn_house1_bed_lamd.grid(column=2, row=8)

lbl_house1_bed_lamd_status = Label(window, text="- выключено", font=def_txt_font)
lbl_house1_bed_lamd_status.grid(column=3, row=8)

btn_house1_hot_tub = Button(window, text="Джакузи", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house1_hot_tub)
btn_house1_hot_tub.grid(column=2, row=9)

lbl_house1_hot_tub_status = Label(window, text="- выключено", font=def_txt_font)
lbl_house1_hot_tub_status.grid(column=3, row=9)
buttons.append([btn_house1_all_light, btn_house1_bed_lamd, btn_house1_cook_plate, btn_house1_freez_down, btn_house1_freez_up, btn_house1_hot_tub, btn_house1_oven])

#Зона Дом №2
lbl_house2_title = Label(window,text="Коттедж №2" , font= main_txt_font)
lbl_house2_title.grid(column=4, row=0, columnspan=2)

lbl_house2_status = Label(window, text="Отключено", font=main_txt_font, fg="red")
lbl_house2_status.grid(column=4, row=1, columnspan=2)

lbl_house2_money_val = Label(window, text="Счёт: 0 px", font=def_txt_font)
lbl_house2_money_val.grid(column=4, row=2,columnspan=2 )

btn_house2_cook_plate = Button(window, text="Плита", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house2_cook_plate)
btn_house2_cook_plate.grid(column=4, row=3)

lbl_house2_cook_plate_status = Label(window, text = "- выключено", font=def_txt_font)
lbl_house2_cook_plate_status.grid(column=5, row=3)

btn_house2_oven = Button(window, text="Духовка", font = def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house2_oven)
btn_house2_oven.grid(column=4, row=4)

lbl_house2_oven_status = Label(window, text="- выключено", font=def_txt_font)
lbl_house2_oven_status.grid(column=5, row=4)

btn_house2_freez_up = Button(window, text="Холодильник", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house2_freez_up)
btn_house2_freez_up.grid(column=4, row=5)

lbl_house2_freez_up_status = Label(window, text="- выключено", font=def_txt_font)
lbl_house2_freez_up_status.grid(column=5, row=5)

btn_house2_freez_down = Button(window, text="Морозильник", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house2_freez_down)
btn_house2_freez_down.grid(column=4, row=6)

lbl_house2_freez_down_status = Label(window, text="- выключено", font=def_txt_font)
lbl_house2_freez_down_status.grid(column=5, row=6)

btn_house2_all_light = Button(window, text="Общий свет", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house2_all_light)
btn_house2_all_light.grid(column=4, row=7)

lbl_house2_all_light_status = Label(window, text="- выключено", font=def_txt_font)
lbl_house2_all_light_status.grid(column=5, row=7)

btn_house2_bed_lamd = Button(window, text="Прикроватные лампы", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house2_bed_lamd)
btn_house2_bed_lamd.grid(column=4, row=8)

lbl_house2_bed_lamd_status = Label(window, text="- выключено", font=def_txt_font)
lbl_house2_bed_lamd_status.grid(column=5, row=8)

btn_house2_tv = Button(window, text="Телевизор", font=def_txt_font, height = 1, width=20, activeforeground = "grey", command =click_btn_house2_tv)
btn_house2_tv.grid(column=4, row=9)

lbl_house2_tv_status = Label(window, text="- выключено", font=def_txt_font)
lbl_house2_tv_status.grid(column=5, row=9)
buttons.append([btn_house2_all_light, btn_house2_bed_lamd, btn_house2_cook_plate, btn_house2_freez_down, btn_house2_freez_up, btn_house2_tv, btn_house1_oven])
#Нижнее меню кнопок
btn_exit = Button(window, text= "Выход", font=main_txt_font, height = 1, width=20, activeforeground = "grey", command =exit_pr)
btn_exit.grid(row=18, column=5)

btn_all_on = Button(window, text="Включить все устройства",font=def_txt_font, height = 1, width=30, activeforeground = "grey", command =all_on)
btn_all_on.grid(row=18, column=3)

btn_all_off = Button(window, text="Выключить все устройства",font=def_txt_font, height = 1, width=30, activeforeground = "grey", command =all_off)
btn_all_off.grid(row=18, column=4)

btn_work_type = Button(window, text="Переключение режима работы (ручной/автоматический)",font=def_txt_font, height = 1, width=50, activeforeground = "grey", command =work_type)
btn_work_type.grid(row=18, column=1, columnspan=2)

btn_start_car_control = Button(window, text="Пульт ДУ", font= def_txt_font, command=click_btn_start_car_control, height = 1, width=20, activeforeground = "grey")
btn_start_car_control.grid(row=18, column = 0)

buttons_mass =  []
for btn_mass in buttons:
    for btn in btn_mass:
        buttons_mass.append(btn)
info_update()
lbl_condition_check()




window.mainloop()