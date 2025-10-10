
import random

matematica_diaria = [
    "Numeros operacionales",
    "Algebra",
    "Geometria",
    "Trigonometria",
    "Calculo",
    "Estadistica",
    "Probabilidad",
    "Matematica Discreta",
    "Teoria de Números"
]

tema_del_dia = random.choice(matematica_diaria)

print(f"El tema de matemáticas para hoy es: {tema_del_dia}")