EDAD_MINIMA = 21
edad = int(input("Ingrese su edad:  "))
categoria = input("Ingrese su categoria: (A, B, C, D, E, F, G,)")
if edad >= EDAD_MINIMA and (categoria == "D" or categoria =="d"):
    print("puede conducir ambulancias")
else:
    print("no puede conducir ambulancias")
