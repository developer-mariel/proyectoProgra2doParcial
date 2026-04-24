estu = {394704: "Carlos Terrazas",394611: "Mariel Rivas",394570: "Ricardo Robles",    394412: "Elias Campos"}
for matricula in estu:
    print("--- Evaluando estudiante ---")
    print("Nombre:", estu[matricula])
    print("Matricula:", matricula)

    curso = input("Materia a evaluar: ")

    # Calificación 1
    while True:
        try:
            calif1 = float(input("Teclea la primer calificación: "))
            if 0 <= calif1 <= 10:
                break
            else:
                print("Error: la calificación debe estar entre 0 y 10")
        except:
            print("Error: debes ingresar un número")

    # Calificación 2
    while True:
        try:
            calif2 = float(input("Teclea la segunda calificación: "))
            if 0 <= calif2 <= 10:
                break
            else:
                print("Error: la calificación debe estar entre 0 y 10")
        except:
            print("Error: debes ingresar un número")

    # Calificación 3
    while True:
        try:
            calif3 = float(input("Teclea la tercera calificación: "))
            if 0 <= calif3 <= 10:
                break
            else:
                print("Error: la calificación debe estar entre 0 y 10")
        except:
            print("Error: debes ingresar un número")

    promedio = (calif1 * 0.3) + (calif2 * 0.3) + (calif3 * 0.4)

    print("Promedio =", promedio)

    if promedio >= 7:
        print("Resultado: APROBADO")
    else:
        print("Resultado: REPROBADO")