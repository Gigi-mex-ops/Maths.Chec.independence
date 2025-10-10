#creando slicing 

numeros_slicing= [0, 1, 10, 20, 30, 40, 50]

print (numeros_slicing[0:3])
print (numeros_slicing[:3])
print (numeros_slicing[3:])

for numeros in numeros_slicing:
    print(numeros)



# Modificar una parte de la lista usando slicing
numeros_slicing[2:5] = [100, 200, 300]
print("Lista modificada:", numeros_slicing)

# Invertir la lista usando slicing
print("Lista invertida:", numeros_slicing[::-1])