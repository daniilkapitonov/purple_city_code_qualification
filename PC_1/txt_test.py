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

file_list = ["администрация.txt", "батареи.txt", "больница.txt", "вода.txt","выработка.txt", "дом_1.txt", "дом_2.txt",
     "дома.txt","здания.txt", "мчс.txt","потребление.txt", "ges_s.txt", "output.txt", "pred.txt","administration.txt", 
     "hospital.txt", "house_1.txt", "house_2.txt", "mus.txt", "ges.txt"]
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


print (house_1_rele_file)











# str_print = ""
# f = open(adm_rele_file, "r")
# h_2 = f.read().split("\n")
# f.close()
# h_2= h_2[:-1]
# str_print += f"Администрация: реле - {h_2}, "
# f_b = open (energy_consumption_file, "r")
# f_w = open (water_file, "r")
# adm_energy_con = int(h_2[0])*20 + int(h_2[1])*120 + int(h_2[2])*30 + int(h_2[3])*10 
# adm_energy_con = round(float(adm_energy_con)/100, 3)
# print(adm_energy_con)
# #str_print += f"потребление - {adm_energy_con}. "
# f = open(adm_house_file, "w")
# batary_con = float(f_b.read().split("\n")[0])
# print(batary_con)
# batary_con += adm_energy_con
# print(batary_con)
# batary_per = "9"
# f.write("1"+"\n"+batary_per+"\n"+f_w.read().split("\n")[0]+"\n"+str(adm_energy_con)+"\n")
# f.close()
# f_b.close()
# f_b = open (energy_consumption_file, "w")
# f_b.write(str(batary_con)[:5]+"\n")
# f_b.close()
# f_w.close()

# print(str_print)

if value[0] == "0":
    lbl_ges_water_in_status.configure(text= "- не активно")
else:
    lbl_ges_water_in_status.configure(text= "- активно")

if value[1] == "0":
    lbl_ges_water_out_status.configure(text= "- не активно")
else:
    lbl_ges_water_out_status.configure(text= "- активно")