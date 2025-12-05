# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 13:48:52 2025

@author: phili
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
communes = []
with open("donnees_2008.csv", newline= '') as csvfile :
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        communes.append(row)
        
#print(communes)
del(communes[0])


Yonne = []
print(Yonne)

for i in range(len(communes)):
    if communes[i][6]=='Appoigny':
        Yonne.append(communes[i][9]);
        
    if(communes[i][6]=='Auxerre'):
        Yonne.append(communes[i][9])
        
    if(communes[i][6]=='Monéteau'):
        Yonne.append(communes[i][9])
        
    if(communes[i][6]=='Perrigny'):
        if(communes[i][9]=='1203'):
            Yonne.append(communes[i][9])
            
        
    if(communes[i][6]=='Saint-Georges-sur-Baulche'):
        Yonne.append(communes[i][9])
        
print(Yonne)
moy2008 = 0


for j in range(len(Yonne)):
    moy2008 = moy2008+int(Yonne[j])   
moy2008 = moy2008/len(Yonne)
print(moy2008)


commune2 = []
with open("donnees_2016.csv", newline= '') as csvfile :
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        commune2.append(row)
        
#print(commune2)
del(commune2[0])


Yonne2 = []
codcom = []

for k in range(len(commune2)):
    if commune2[k][6]=='Appoigny':
        Yonne2.append(commune2[k][9]);
        codcom.append(commune2[k][5])
    if(commune2[k][6]=='Auxerre'):
        Yonne2.append(commune2[k][9]);
        codcom.append(commune2[k][5])
    if(commune2[k][6]=='Monéteau'):
        Yonne2.append(commune2[k][9]);
        codcom.append(commune2[k][5])
    if(commune2[k][6]=='Perrigny'):
        if(commune2[k][9]=='1310'):
            Yonne2.append(commune2[k][9])
            codcom.append(commune2[k][5])
    if(commune2[k][6]=='Saint-Georges-sur-Baulche'):
        Yonne2.append(commune2[k][9]);
        codcom.append(commune2[k][5])
print(Yonne2)
print(codcom)
moy2016 = 0


for j in range(len(Yonne2)):
    moy2016 = moy2016+int(Yonne2[j])   
moy2016 = moy2016/len(Yonne2)
print(moy2016)


commune3 = []
with open("donnees_2021.csv", newline= '') as csvfile :
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        commune3.append(row)
        
#print(commune3)
del(commune3[0])

g=0

Yonne3 = []

for k in range(len(commune3)):
    if commune3[k][2]=='89013':
        Yonne3.append(commune3[k][5])
    if(commune3[k][2]=='89024'):
        Yonne3.append(commune3[k][5])
    if(commune3[k][2]=='89263'):
        Yonne3.append(commune3[k][5])
    if(commune3[k][2]=='89295'):
        Yonne3.append(commune3[k][5])
    if(commune3[k][2]=='89346'):
        Yonne3.append(commune3[k][5])
    
print(Yonne3)
moy2021 = 0


for j in range(len(Yonne3)):
    moy2021 = moy2021+int(Yonne3[j])   
moy2021 = moy2021/len(Yonne3)
print(moy2021)





commune4 = []
with open("donnees_2023.csv", newline= '') as csvfile :
    reader=csv.reader(csvfile,delimiter=';')
    for row in reader:
        commune4.append(row)
        
#print(communes)
del(commune4[0])


Yonne4 = []

for i in range(len(commune4)):
    if commune4[i][7]=='Appoigny':
        Yonne4.append(commune4[i][10]);
        
    if(commune4[i][7]=='Auxerre'):
        Yonne4.append(commune4[i][10])
        
    if(commune4[i][7]=='Monéteau'):
        Yonne4.append(commune4[i][10])
        
    if(commune4[i][7]=='Perrigny'):
        if(commune4[i][10]=='1292'):    
            Yonne4.append(commune4[i][10])
            
        
    if(commune4[i][7]=='Saint-Georges-sur-Baulche'):
        Yonne4.append(commune4[i][10])
        
print(Yonne4)
moy2023 = 0


for j in range(len(Yonne4)):
    moy2023 = moy2023+int(Yonne4[j])   
moy2023 = moy2023/len(Yonne4)
print(moy2023)

moyennes = [moy2008,moy2016,moy2021,moy2023]

x = ["2008","2016","2021","2023"]

y = np.array(moyennes)
plt.plot(x,y,marker='o')
plt.xlabel("Année")
plt.ylabel('Population')
plt.title("Population de l'aglomération immédiate")
plt.show()
