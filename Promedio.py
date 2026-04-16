estu={394704: "Carlos Terrazas",394611: "Mariel Rivas",394570: "Ricardo Robles",394412: "Elias Campos"}
mati=int(input("Matricula del estudiante a evaluar:"))
if mati in estu:
 print("nombre:",estu[mati])
#for matricula in estu:
 #print("Estudiante: estu[matricula] Matricula: [matricula]")
 curso=(input("Materia a evaluar:"))
 calif1=float(input("Teclea la primer calificación: "))
 calif2=float(input("Teclea la segunda calificación: "))
 calif3=float(input("Teclea la tercera calificación: "))
 promedio=(calif1*0.3)+(calif2*0.3)+(calif3*0.4)
 print("Promedio= ",promedio)