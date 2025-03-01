open1 = open("inspired.txt", "r")  
open2 = open("inspiredupdated.txt", "w")  

cont = open1.readlines()  

for line in cont:  
    line = line.strip()  
    if "sky" in line:  
        open2.write(line + " — Enjoy the view!\n")  
    elif "breeze" in line:  
        open2.write(line + " — Let it lift you up!\n")  
    elif "peace" in line:  
        open2.write(line + " — Find your calm.\n")  
    else:  
        open2.write(line + " — Keep going!\n")  

open2.close()  

open2 = open("inspiredupdated.txt", "r")  
cont1 = open2.read()  
print(cont1)  

open1.close()  
open2.close()