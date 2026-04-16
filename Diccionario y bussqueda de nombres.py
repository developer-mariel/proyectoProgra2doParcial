alumnos = {394704: "Carlos Terrazas",394611: "Mariel Rivas",394570: "Ricardo Robles",394412: "Elias Campos"}
while True:
        print("--- BUSQUEDA DE ALUMNO ---")
        
        try:
            mat = int(input("Ingresa la matricula (0 para salir): "))

            if mat == 0:
                print("Saliendo de la busqueda...")
                break

            if mat in alumnos:
                print("Alumno encontrado")
                print("Nombre:", alumnos[mat])
                print("Matricula:", mat)
            else:
                print("El alumno no esta en el equipo")

        except:
            print("Error: debes ingresar un numero")




