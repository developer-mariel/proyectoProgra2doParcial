estu = {
    394704: "Carlos Terrazas",
    394611: "Mariel Rivas",
    394570: "Ricardo Robles",
    394412: "Elias Campos"
}

for matricula in estu:
    print("--- Evaluando estudiante ---")
    print("Nombre:", estu[matricula])
    print("Matricula:", matricula)

    continuar = "s"

    while continuar == "s":
        curso = input("Materia a evaluar: ")

        # Calificación 1
        calif1 = float(input("Teclea la primer calificación: "))
        while calif1 < 0 or calif1 > 10:
            print("Error: la calificación debe estar entre 0 y 10")
            calif1 = float(input("Teclea la primer calificación: "))

        # Calificación 2
        calif2 = float(input("Teclea la segunda calificación: "))
        while calif2 < 0 or calif2 > 10:
            print("Error: la calificación debe estar entre 0 y 10")
            calif2 = float(input("Teclea la segunda calificación: "))

        # Calificación 3
        calif3 = float(input("Teclea la tercera calificación: "))
        while calif3 < 0 or calif3 > 10:
            print("Error: la calificación debe estar entre 0 y 10")
            calif3 = float(input("Teclea la tercera calificación: "))

        promedio = (calif1 * 0.3) + (calif2 * 0.3) + (calif3 * 0.4)

        print("Materia:", curso)
        print("Promedio =", promedio)

        if promedio >= 7:
            print("Resultado: APROBADO")
        else:
            print("Resultado: REPROBADO")

        continuar = input("¿Quieres calcular otra materia para este alumno? (si/no): ").lower()

    print("Pasando al siguiente estudiante...")