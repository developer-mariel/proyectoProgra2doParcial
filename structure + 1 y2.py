import sys

import pyfiglet
import time
from colorama import init, Fore, Back, Style
init()
def ppl():
    alumnos={394611: "Mariel Rivas", 394570: "Ricardo Robles", 394704:"Carlos Terrazas", 394412:"Elías Campos"}
    opc = 0
    #podemos poner todo con los colores de los 4 fantasticos xd
    while opc!=5:
        print(Fore.BLUE+"")
        print(" Menú")
        print(" 1) Búsqueda de alumno")
        print(" 2) Promedio por integrante")
        print(" 3) Derecho a no ordinario")
        print(" 4) El equipo más pro")
        print(" 5) Salir")
        print("                ")
        opc=int(input(" Ingresa la selección: "))
        match opc:
            case 1:
                while True:
                    print("--- BUSQUEDA DE ALUMNO ---")

                    try:
                        mat = int(input("Ingresa la matricula (0 para salir): "))
                    except:
                        print("Error: debes ingresar un número")
                        continue   # regresa al inicio del while
                    if mat == 0:
                        print("Saliendo de la busqueda...")
                        break
                    if mat in alumnos:
                        print("Alumno encontrado")
                        print("Nombre:", alumnos[mat])
                        print("Matricula:", mat)
                    else:
                        print("El alumno no esta en el equipo")
            case 2:
                for matricula in alumnos:
                    print("---Promedio por integrante---")
                    print("Nombre:", alumnos[matricula])
                    print("Matricula:", matricula)
                    curso= input("Materia a evaluar: ")
                    #Calificacion 1
                    while True:
                        try:
                            calif1= float(input("Teclea la primer calificación:"))
                            if 0 <= calif1 <=10:
                                break
                            else:
                                print("Error: la calificación debe estar entre 0 y 10")
                        except:
                            print("Error: debes ingresar un número")
                    #Calificación 2
                    while True:
                        try:
                            calif2= float(input("Teclea la segunda calificación:"))
                            if 0 <= calif2 <=10:
                                break
                            else:
                                print("Error: la calificación debe estar entre 0 y 10")
                        except:
                            print("Error: debes ingresar un número")
                    #Calificacion 3
                    while True:
                        try:
                            calif3= float(input("Teclea la tercera calificación:"))
                            if 0 <= calif3 <=10:
                                break
                            else:
                                print("Error: la calificación debe estar entre 0 y 10")
                        except:
                            print("Error: debes ingresar un número")
                    promedio=(calif1 * 0.3) + (calif2 * 0.3) + (calif3 * 0.4)
                    print("Promedio =", promedio)
                    if promedio >=7:
                        print("Resutado: APROBADO")
                    else:
                        print("Resultado: REPROBADO")
            case 3:
                print("--- Permiso para el no ordinario por equipo ---")
                for matricula, nombre in alumnos.items():
                    print(f"\nEvaluando estatus de: {nombre} ({matricula})")
                    
                    while True:
                        try:
                            materias_cursadas = int(input("¿Cuántas materias has cursado? "))
                            if 1 <= materias_cursadas <= 20:
                                break
                            else:
                                print("Error: debes ingresar un número entero entre 1 y 20.")
                        except ValueError:
                            print("Error: entrada inválida. Por favor, ingresa un número entero.")

                    while True:
                        try:
                            materias_aprobadas = int(input("¿Cuántas materias has aprobado? "))
                            if 0 <= materias_aprobadas <= materias_cursadas:
                                break
                            else:
                                print(f"Error: debes ingresar un número entero entre 0 y {materias_cursadas}.")
                        except ValueError:
                            print("Error: entrada inválida. Por favor, ingresa un número entero.")

                    if materias_cursadas >= 2:
                        porcentaje_aprobacion = (materias_aprobadas / materias_cursadas) * 100
                        if porcentaje_aprobacion >= 50:
                            print("Tiene permitido realizar el examen no ordinario.")
                        
                        else:
                            print("No tiene derecho al no ordinario. Deberá repetir el semestre o materias.")
                    else:
                        print("No tiene derecho al no ordinario (debe cursar 2 o más materias). Deberá repetir la materia no acreditada.")

            case 4:
                txt1=pyfiglet.figlet_format("        LOS", font="slant")
                txt2=pyfiglet.figlet_format("FANTASTICOS", font="slant")
                print(txt1)
                print("                  **************")
                print("              **********************")
                print("           ****************************")
                print("       ************            ************")
                print("      *********                    *********")
                print("     *********       //      ||      *********")
                print("    ********        //       ||        ********")
                print("   ********        //        ||         ********")
                print("  ********        //         ||          ********")
                print("  ********        -_-_-_-_-_-||          ********")
                print("  ********                   ||          ********")
                print("   ********                  ||         ********")
                print("    ********                 ||        ********")
                print("     *********               ||      *********")
                print("      *********                    *********")
                print("       ************            ************")
                print("           ****************************")
                print("              **********************")
                print("                  **************")
                print(txt2)
                print(" Carlos Terrazas Rugelio - 394704")
                print(" Ricardo Robles Mancha  - 394570")
                print(" Elías Campos García - 394412")
                print(" Mariel Rivas Martínez - 394611")
                print("  ")   
            case 5:
                print(" Saliendo del programa...")
                time.sleep(1)
                break
            case _:
                print(" Ingresa un caracter válido.")
        print("")        
        input(" Presiona cualquier tecla para continuar")            

if __name__ == "__main__":
    ppl()