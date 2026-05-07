import os
import time
#Archivo de excel archivo.xlsx
import openpyxl
from colorama import init, Fore, Back, Style
init()



#variables globales
x=0
wb=""
#Función para abrir el archivo de excel
def abrir_excel():
  global x,wb #Se modifican las variables globales
  try: 
#Workbook o libro de excel (la diagonal para usar en la dirección es / ):
    wb=openpyxl.load_workbook("C:/Users/ianterrazasrugelio/Documents/Trabajos de la universidad/Segundo semestre/PROGRAM/Python/3ER PARCIAL/PROING26.xlsx") #pip install openpyxl
    x=1
    print("Archivo abierto con éxito")
  except:
     print("Algo se puso raro...\U0001F914")
     x=0
  return(x)



def ppal():
  Edo=abrir_excel()#regresa un 1 o un 0
  if Edo==1: #Si se pudo abrir
    opc=0 
    while opc!=6:
     print(Fore.YELLOW+" ADMINISTRACIÓN DE EQUIPOS EN EXCEL ","\n"
     "1.CREAR EQUIPO"      
     "2.BUSQUEDA POR ALUMNO","\n"
     "3.CALIFICACIONES Y PROMEDIO DEL EQUIPO","\n"
     "4.PERMISO PARA EL NO ORDINARIO POR EQUIPO","\n"
     "5.EQUIPAZO","\n"
     "6.SALIR")
     opc=int(input("Ingresa una opción: "))
     print(" "+ Style.RESET_ALL)
     match opc:
       case 1:
         print(Back.BLUE+"1.CREAR EQUIPO"+ Style.RESET_ALL)
       case 2:
         print(Back.BLUE+"2.BUSQUEDA POR ALUMNO"+ Style.RESET_ALL)
       case 3:
         print(Back.BLUE+"3.CALIFICACIONES Y PROMEDIO DEL EQUIPO"+ Style.RESET_ALL)
       case 4:
         print(Back.BLUE+"4.PERMISO PARA EL NO ORDINARIO POR EQUIPO"+ Style.RESET_ALL)
       case 5:
         print(Back.BLUE+"5.EQUIPAZO"+ Style.RESET_ALL)
       case 6:
         print(Back.BLUE+"6.SALIR"+ Style.RESET_ALL)

  else: #Si Edo=0
     print("El archivo no esta creado o esta abierto \U0001F6A7")


if __name__=="__main__":
  ppal()  