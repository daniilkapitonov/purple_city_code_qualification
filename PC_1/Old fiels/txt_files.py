import time
import os
import datetime
# f = open("/home/pi/Desktop/Demo/txt_files/send_message.txt", 'r')
# code = str(f.read())
# print(code)
# f.close()
# str_resive = "3214_3412_12"
# num_1 = str_resive.split("_")[0]
# num_2 = str_resive.split("_")[1]
# num_3 = str_resive.split("_")[2]
# print (num_1, num_2, num_3)

# data = datetime.datetime.now()
# data = data.strftime("%H")
# print(data)

# f = open ("/home/pi/Desktop/Demo/txt_files/data_for_web.txt", "w")
# f.write(num_1+'\n'+num_2+'\n'+num_3+'\n'+data)
# f.close()
import time
def step():
    for i in range(1,500):
        for j in range(1,500):
            i**j
            
print("Start SYS")
start = time.time()
step()
end = time.time()
print(end-start)



