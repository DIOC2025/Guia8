"""Caso 4: Registro de participación estudiantil por carrera en la UAM
Desarrolle un programa que registre la participación de estudiantes de la UAM en actividades
extracurriculares por carrera. Considere tres carreras (por ejemplo: Sistemas, Marketing y
Derecho), cada una con tres años académicos, y cada año con dos secciones. Por cada
sección, se debe registrar cuántos estudiantes participaron. El programa debe mostrar el total
por carrera y el total general de participantes. Utilice bucles anidados."""

print("Registro de participación estudiantil por carrera en la UAM\n")

# Lista de carreras
carreras = ["Sistemas", "Marketing", "Derecho"]
total_general = 0  # Acumula todos los participantes de todas las carreras

# Recorremos cada carrera
for idx, carrera in enumerate(carreras, start=1):
    print(f"=== Carrera {idx}: {carrera} ===")
    total_carrera = 0  # Acumula los participantes de esta carrera

    # Para cada uno de los 3 años académicos
    for año in range(1, 4):
        # Para cada una de las 2 secciones (A y B)
        for seccion in ("A", "B"):
            prompt = f"Ingrese número de participantes en {carrera}, Año {año}, Sección {seccion}: "
            participantes = int(input(prompt))
            total_carrera += participantes

    # Fin de la carrera: mostramos su total
    print(f"Total participantes en {carrera}: {total_carrera}\n")
    total_general += total_carrera

# Al final, imprimimos el total general de todas las carreras
print("=== Resumen Final ===")
for idx, carrera in enumerate(carreras, start=1):
    # (Si quisieras volver a mostrar cada total_carrera, podrías almacenarlos en una lista)
    pass
print(f"Total general de participantes en todas las carreras: {total_general}")