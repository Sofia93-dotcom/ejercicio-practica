#pedir la cantidad inicial y la cantidad de horas y calcular cuantas bacterias habra en total
B_inicial=int(input("Ingrese la cantidad de bacterias:"))
horas=int(input("Ingrese la cantidad de horas:"))
B= B_inicial*(2**horas)
print(f" la cantidad total de bacterias ¨{B}")

