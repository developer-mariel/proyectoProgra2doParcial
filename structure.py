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
                print("Aquí debe buscar por matrícula")
                print("Si encuentra al alumno indica que se encontró y despliega nombre")
                print("Si no lo encuentra indica que no está en el equipo")
            case 2:
                print("Comienza con el nombre de quién evaluará")
                print("Pide la materia")
                print("Luego pedirá c/parcial")
                print("Para c/parcial se verfica validez de la calificacion")
                print("Calculará y (opcional) desplegará promedio") 
                print("Indicará si acreditó la materia")   
            case 3:
                print("Permiso para el no ordinario por equipo")
                #podemos pintar de rojo cuando no tenga derecho y de verde cuando sí
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
    