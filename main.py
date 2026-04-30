import sys
from typing import Dict

# Datos del equipo desarrollador
TEAM_NAME = "Los 4 fantásticos"
TEAM_MEMBERS: Dict[str, str] = {
    "394570": "Ricardo Robles Mancha",
    "394704": "Carlos Terrazas Rugelio",
    "394412": "Elías Campos García",
    "394611": "Mariel Rivas Martínez"
}

def get_valid_int(prompt: str, min_val: int = 0, max_val: int = sys.maxsize) -> int:
    """
    Solicita un número entero y valida que se encuentre dentro del rango especificado
    y que efectivamente sea un entero, manejando excepciones para evitar que el programa falle.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"⚠️ Error: Debes ingresar un número entero entre {min_val} y {max_val}.")
        except ValueError:
            print("⚠️ Error: Entrada inválida. Por favor, ingresa un número entero.")

def get_valid_float(prompt: str, min_val: float = 0.0, max_val: float = 10.0) -> float:
    """
    Solicita un número de punto flotante y valida que esté dentro del rango especificado.
    Maneja excepciones (try-except) para capturar entradas que no sean números.
    """
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"⚠️ Error: La calificación debe estar en un rango de {min_val} a {max_val}.")
        except ValueError:
            print("⚠️ Error: Entrada inválida. Por favor, ingresa un número válido.")

def buscar_alumno() -> None:
    """Opción 1: Busca a un alumno por medio de su matrícula dentro del diccionario del equipo."""
    print("\n--- 1. BÚSQUEDA DE UN ALUMNO ---")
    matricula = input("Ingresa la matrícula del alumno a buscar: ").strip()
    
    if matricula in TEAM_MEMBERS:
        print(f"✅ Alumno encontrado: {TEAM_MEMBERS[matricula]}")
    else:
        print("❌ El alumno no está en el equipo desarrollador.")

def calificaciones_y_promedio() -> None:
    """Opción 2: Calcula el promedio del equipo para una materia preestablecida."""
    print("\n--- 2. CALIFICACIONES Y PROMEDIO DEL EQUIPO ---")
    materia = input("Ingresa el nombre de la materia (ej. Programación): ").strip() or "Programación"
    
    # Uso de la estructura condicional y el ciclo for requeridos en la rúbrica.
    for matricula, nombre in TEAM_MEMBERS.items():
        print(f"\nIngresando calificaciones para: {nombre} ({matricula}) en [{materia}]")
        parcial1 = get_valid_float("  -> Parcial 1: ")
        parcial2 = get_valid_float("  -> Parcial 2: ")
        parcial3 = get_valid_float("  -> Parcial 3: ")
        
        promedio = (parcial1 + parcial2 + parcial3) / 3.0
        print(f"  📌 Promedio final: {promedio:.2f}")
        
        if promedio >= 6.0:  # Suponiendo escala 0-10 aprobando con 6.
            print("  🎉 Resultado: ACREDITÓ la materia.")
        else:
            print("  ❌ Resultado: NO ACREDITÓ la materia.")

def permiso_no_ordinario() -> None:
    """
    Opción 3: Evalúa si los integrantes del equipo tienen derecho a presentar el examen no ordinario 
    dependiendo de las condiciones establecidas en el Artículo 61.
    """
    print("\n--- 3. PERMISO PARA EL NO ORDINARIO POR EQUIPO ---")
    
    for matricula, nombre in TEAM_MEMBERS.items():
        print(f"\nEvaluando estatus de: {nombre} ({matricula})")
        materias_cursadas = get_valid_int("  -> ¿Cuántas materias cursa en total?: ", min_val=1, max_val=20)
        materias_aprobadas = get_valid_int(f"  -> De esas {materias_cursadas}, ¿cuántas aprobó?: ", min_val=0, max_val=materias_cursadas)
        
        # Lógica del Artículo 61
        if materias_cursadas >= 2:
            porcentaje_aprobacion = (materias_aprobadas / materias_cursadas) * 100
            if porcentaje_aprobacion >= 50.0:
                print("  ✅ Estatus: TIENE PERMITIDO realizar el examen no ordinario.")
            else:
                print("  ❌ Estatus: NO TIENE DERECHO al no ordinario. DEBERÁ REPETIR el semestre o materias.")
        else:
            print("  ❌ Estatus: NO TIENE DERECHO al no ordinario (debe cursar 2 o más materias). DEBERÁ REPETIR la materia no acreditada.")

def equipo_desarrollador() -> None:
    """Opción 4: Imprime el nombre del equipo y sus integrantes."""
    print("\n--- 4. EQUIPO DESARROLLADOR ---")
    print(f"Nombre del equipo: 🚀 {TEAM_NAME} 🚀")
    print("Integrantes:")
    for matricula, nombre in TEAM_MEMBERS.items():
        print(f" - {nombre} (Matrícula: {matricula})")

def main() -> None:
    """
    Controlador principal del programa. 
    Muestra el menú y maneja las opciones del usuario con un flujo continuo usando 'while' y 'match-case'.
    """
    print("==================================================")
    print("   UNIVERSIDAD AUTÓNOMA DE CHIHUAHUA - FING")
    print("   Programación para Ingenieros - 2do Parcial")
    print("==================================================")
    
    while True:
        print("\n" + "="*40)
        print("               MENÚ PRINCIPAL")
        print("="*40)
        print("1. Búsqueda de un alumno")
        print("2. Calificaciones y promedio del equipo")
        print("3. Permiso para el no ordinario por equipo")
        print("4. Equipo desarrollador")
        print("5. Salir")
        print("="*40)
        
        opcion = get_valid_int("Seleccione una opción (1-5): ", 1, 5)
        
        # Uso de match-case (requerido por la rúbrica)
        match opcion:
            case 1:
                buscar_alumno()
            case 2:
                calificaciones_y_promedio()
            case 3:
                permiso_no_ordinario()
            case 4:
                equipo_desarrollador()
            case 5:
                print("\nSaliendo del programa... ¡Hasta luego!")
                break
            case _:
                # El validador ya impide llegar aquí, pero por seguridad y estructura se pone.
                print("Opción no reconocida.")

if __name__ == "__main__":
    main()
