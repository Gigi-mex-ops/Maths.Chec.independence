print  ("Bienvenido a mi calculadora")
print("elige una opcion")


#eliges el numero que decees que se imprima 
num1 = float(input("escribe el primer numero = "))
num2 = float(input("escribe el segundo numero = "))

"""
eliges la operacion que quieres realizar ya sea 
suma +
resta -
multiplicacion * || o Divicion / 
"""
operacion = input("escribe la operacion(+,-,*,/):")

#escribo if porque quiero que mi resultado de la suma de num1 y num 2
if operacion == "+":
    
    resultado = num1 + num2
 #escribo elif porque eligo otro tipo de operacion para calcular num1 y num2 
 #para mi elif es tipo si a no quiero suma elijo otra cosa es como quiero helado o galletas o pizza :) 
elif operacion == "-":
    
    resultado = num1 - num2 
    
elif operacion == "*":
    
    resultado = num1 * num2 
    
elif operacion == "/":
    
    resultado = num1 * num2 
    
else:

 resultado = "operacion no valida"

print ("el resultado es =:",resultado)


