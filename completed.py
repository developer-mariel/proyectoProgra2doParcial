import sys
import pyfiglet
from pyfiglet import figlet_format
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
        
        try:
            opc=int(input(" Ingresa la selección: "))
        except ValueError:
            print(" Error: Ingresa un caracter válido.")
            time.sleep(1)
            continue
        print("")
        match opc:
            case 1:
                while True:
                    print("--- BUSQUEDA DE ALUMNO ---")
                    try:
                        mat = int(input("Ingresa la matricula (0 para salir): "))
                    except ValueError:
                        print("Error: debes ingresar un número")
                        continue   # regresa al inicio del while
                    if mat == 0:
                        print("Saliendo de la busqueda...")
                        break
                    if mat in alumnos:
                        print("Alumno encontrado")
                        print("Nombre:", alumnos[mat])
                        print("Matricula:", mat) #matricula ya la sabe porque la acaba de ingresar
                    else:
                        print("El alumno no esta en el equipo")
            case 2:
                print(figlet_format("Promedio por integrante", font="contessa")) #doom o contessa
                for matricula in alumnos:
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
                        except ValueError:
                            print("Error: debes ingresar un número")
                    #Calificación 2
                    while True:
                        try:
                            calif2= float(input("Teclea la segunda calificación:"))
                            if 0 <= calif2 <=10:
                                break
                            else:
                                print("Error: la calificación debe estar entre 0 y 10")
                        except ValueError:
                            print("Error: debes ingresar un número")
                    #Calificacion 3
                    while True:
                        try:
                            calif3= float(input("Teclea la tercera calificación:"))
                            if 0 <= calif3 <=10:
                                break
                            else:
                                print("Error: la calificación debe estar entre 0 y 10")
                        except ValueError:
                            print("Error: debes ingresar un número")
                    promedio=(calif1 * 0.3) + (calif2 * 0.3) + (calif3 * 0.4)
                    time.sleep(1)
                    print("Promedio de", curso, "=", promedio)
                    time.sleep(1)
                    if promedio >=7:
                        print("Resultado: APROBADO")
                    else:
                        print("Resultado: REPROBADO")
                    print("")    
            case 3:
                print("--------Reporte del Semestre--------")
                
                for alumno in alumnos:
                    print(" ")
                    print("Permiso para no ordinario de",alumnos[alumno]) 
                    while True:
                        answer = input("¿Listo para ver tu progreso del semestre? (S/N): ")
                        if answer.lower() == "n":
                            print("Vaya, ¡pues no malgastes mi tiempo!")
                            break
                        elif answer.lower() == "s" or answer.lower() == "y":    
                            print("¡Continuemos!")
                            while True:
                                try:
                                    materia = int(input("¿Cuántas materias cursaste este semestre?: "))
                                    if 2 <= materia <= 10:
                                        break
                                    else:
                                        print("Error: ninguna carrera cuenta con materias mayores a 10 o menores a 2")
                                except:
                                    print("Error: debes ingresar un número")
                            while True:
                                try:
                                    passed = int(input("Dinos cuantas materias aprobaste: "))
                                    if 0 <= passed <= materia:
                                        break
                                    else:
                                        print("Error: esto no cumple con lo que especificaste")
                                except:
                                    print("Error: debes ingresar un número valido")

                            failed = int(materia - passed)
                            print("Según tu respuesta, las materias que has reprobado son: ", failed)

                            calculo = round(materia/2)

                            if -1 < failed < 1:
                                print("Felicidades, has pasado el semestre sin necesidad de hacer no ordinarios")
                            else:
                                if failed <= calculo:
                                    print("Aunque hayas reprobado una que otra materia, tienes derecho a NO ORDINARIO")
                                else:
                                    print("Lo siento, reprobaste más de la mitad de materias, debes REPETIRLO TODO")
                                    break  
                            break          
                        else:
                            print("Ingresa una respuesta válida")

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
                print(" Ingresa una opción válida.")
        print("")        
        input(" Presiona cualquier tecla para continuar")            

if __name__ == "__main__":
    ppl()