y='02b005330200000561080100 ' 
x = y[6:14]
z=y[12]+y[13]+y[10]+y[11]+y[8]+y[9]+y[6]+y[7]
w = int(z, 16)
print ("Valeur Sigfox :",end =''); print (x)
print ("Compteur 1 en string (déja inversé) :",end =''); print (z)
print ("Compteur en entier :",end =''); print (w)

input('\n\nPress "Enter" to leave')
