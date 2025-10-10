print('Ingreso/verficiacion de edad')

edad_usuario =int(input("que edad tienes? "))

if edad_usuario<18:
    print('NO PUEDES PASAR')
elif edad_usuario>100:
    print('ERROR')    
    
else:
    print("puede pasar")