import serial as sr
import math


# function section ==========================================================================================

def module(acc_list):
    square_list=[]

    for element in acc_list:
        element = element * element

        square_list.append(element)

    module = math.sqrt(sum(square_list))

    return module






print('==========================')
print('a) COM3 Windows')
print('b) COM6 Windows')
print('c) /dev/ttyACM0 Linux ')
print('d) Calibration')
print('==========================')

choose = input('Scegli: ')

if choose == 'a':
     s = sr.Serial('COM3',9600)
elif choose == 'b':
     s = sr.Serial('COM6',9600)
elif choose == 'c':
     s = sr.Serial('/dev/ttyACM0',9600)  #if permission denied run command : sudo chmod 666 /dev/ttyACM0 in terminal shell
else:
    print('No port Selected!')


time_delta = float(input('Lasso di tempo da monitorare: '))

i=0
list_acc_modules = []
j=0

while i<100 :  #  misurazione su 10 secondi (100 decimi)
    reference_value = 16480
    list_raw_acc = []
    list_acc = []
 
    
    a = s.readline()
    raw_data = a.decode()
    
    list_data = raw_data.split()
    list_raw_acc= list_data[0:3]
    
    for element in list_raw_acc:
        element = float(element)
        real_val = 9.81*element / reference_value
       
        list_acc.append(real_val)
        
   
        
        
    modulo = module(list_acc)
    time_stamp = (modulo,round(j,1))
    list_acc_modules.append(time_stamp)
        
    print(time_stamp)
    
    j+=0.1 # contatore della tupla (valore_rilevato, tempo_rilevazione) 
    i+=1

s.close()