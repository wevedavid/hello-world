## Ce code permet de décoder une trame envoyée par un capteur Adeunis Pulse V1.5
#./SigfoxPulse.py

## Valeur de départ (trame envoyée par Sigfox - il s'agit de la trame du 17/09/2018)
start='02a005410200000567080100' 

## Les valeurs décodées manuellement correspondent à 
## Pulse counter index - No errror
## Pulse elec - 577
## Pulse elec - 67687
## Valeur à envoyer chez CarlSoft : ValueCpt(6,7,8,9,10,11,12,13) ou
## ValueCpt(16,17,18,19,20,21,22,23) si brancher sur le deuxieme index...

## Segmentation de la trame
sendingCode = start[0]+start[1]
statusSensor = start[2]+start[3]

## Permet de déterminer la signification du code d'envois
if sendingCode == '00':
    sendingCode = 'Reserved'
elif sendingCode == '02':
    sendingCode = 'Pulse counter index'
elif sendingCode == '03':
    sendingCode = 'Device configuration'
elif sendingCode == '04':
    sendingCode = 'Pusle counter 1 configuration'
elif sendingCode == '05':
    sendingCode = 'Pusle couter 2 configuration'
else :
    sendingCode = 'Code d\'erreur  incohérent'
    
## Permet de déterminer l'état du capteur
statusSensor = int(statusSensor,16)
statusSensor = bin(statusSensor)
statusSensor = statusSensor[len(statusSensor)-3:]

if statusSensor == '000':
    statusSensor = 'No error'
elif statusSensor == '001':
    statusSensor = 'Configuration done'
elif statusSensor == '010':
    statusSensor = 'Low bat'
elif statusSensor == '100':
    statusSensor = 'HW error'
else :
    statusSensor = 'Code d\'erreur  incohérent'

## Permet de déterminer le type du compteur
def TypeCpt(index1,index2):
    typeCpt = start[index1]+start[index2]

    if typeCpt == '00':
        typeCpt = 'Pulse none'
    elif typeCpt == '03':
        typeCpt = 'Pulse auto (Switch)'
    elif typeCpt == '04':
        typeCpt = 'Pulse Gas'
    elif typeCpt == '05':
        typeCpt = 'Pulse Elec'
    elif typeCpt == '06':
        typeCpt = 'Pulse Water 3 wires'
    elif typeCpt == '07':
        typeCpt = 'Pulse Water 4 wires'
    elif typeCpt == '08':
        typeCpt = 'Pulse Water 5 wires'
    elif typeCpt == '09':
        typeCpt = 'Pulse Thermic'
    return typeCpt

## Récupération des bits de valeur du compteur
## Transformation de la valeur hexa en entier
def ValueCpt(index1,index2,index3,index4,index5,index6,index7,index8):
    value = start[index7]+start[index8]+start[index5]+start[index6]+start[index3]+start[index4]+start[index1]+start[index2]
    value = int(value,16)
    return value

## Affichage des différentes valeurs
print ("Trame Sigfox : ",end =''); print (start)
## Valeurs du CAPTEUR
print ("Compteur 1 état du cpt1 : ",end =''); print (sendingCode)
print ("Status du capteur :  ",end =''); print(statusSensor)
## Valeurs du COMPTEUR 1 
print ("Type du compteur 1 :  ",end =''); print(TypeCpt(4,5))
print ("Compteur 1 en entier : ",end =''); print (ValueCpt(6,7,8,9,10,11,12,13))
## Valeurs du COMPTEUR 2
print ("Type du compteur 2 :  ",end =''); print(TypeCpt(14,15))
print ("Compteur 2 en entier : ",end =''); print (ValueCpt(16,17,18,19,20,21,22,23))

input('\n\nPress "Enter" to leave')
