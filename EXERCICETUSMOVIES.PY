#ejercicio para obtener licencia de manejo

age = int(input(("ingrese su edad")))


has_lisence = input("tienes licencia:? (True/False)").lower()=="true"
has_insurance= input("tienes seguro :? (True/False)") .lower() =="true"

result = (age >=18) and has_lisence and has_insurance

print(result)