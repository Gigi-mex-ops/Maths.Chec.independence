# Mini Test de Python 🐍
# Responde escribiendo la opción correcta (A, B, C o D)

preguntas = [
    {
        "pregunta": "1) ¿Cuál es la forma correcta de imprimir en Python?",
        "opciones": {
            "A": "echo('Hola')",
            "B": "print('Hola')",
            "C": "printf('Hola')",
            "D": "mostrar('Hola')"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "2) ¿Qué hace la expresión num == 5?",
        "opciones": {
            "A": "Asigna el valor 5 a num",
            "B": "Comprueba si num es igual a 5",
            "C": "Suma 5 a num",
            "D": "Multiplica num por 5"
        },
        "respuesta": "B"
    },
    {
        "pregunta": "3) ¿Qué tipo de dato es [1, 2, 3]?",
        "opciones": {
            "A": "Lista",
            "B": "Tupla",
            "C": "Diccionario",
            "D": "Entero"
        },
        "respuesta": "A"
    },
    {
        "pregunta": "4) ¿Qué significa el operador 'or'?",
        "opciones": {
            "A": "Que ambas condiciones deben cumplirse",
            "B": "Que ninguna condición debe cumplirse",
            "C": "Que al menos una condición debe cumplirse",
            "D": "Que convierte números en texto"
        },
        "respuesta": "C"
    }
]

puntaje = 0

print("🐍 Mini Test de Python 🐍\n")

for p in preguntas:
    print(p["pregunta"])
    for clave, opcion in p["opciones"].items():
        print(f"   {clave}) {opcion}")
    respuesta = input("Tu respuesta: ").upper()

    if respuesta == p["respuesta"]:
        print("✅ Correcto!\n")
        puntaje += 1
    else:
        print(f"❌ Incorrecto. La respuesta era {p['respuesta']}.\n")

print(f"Tu puntaje final es: {puntaje}/{len(preguntas)}")
