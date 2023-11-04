# Solicitar al usuario el nombre del estudiante y sus notas

def presentación():
    print("---------Ingreso de Datos---------")

def ingresoDatos():
    nombreEstudiante = input("Ingrese el nombre del estudiante: ")
    notasEstudiante = []
    for l in range(4):
        notaFinal = float(input(f"Ingrese la nota {l + 1}: "))
        notasEstudiante.append(notaFinal)

    # Calcular el promedio
    notas = [float(nota) for nota in notasEstudiante]
    promedioEstudiante = sum(notas) / len(notas)

    # Guardar los datos en el archivo "notas.txt"
    with open("notas.txt", "a") as archivo:
        archivo.write(f"Nombre del estudiante: {nombreEstudiante}\n")
        archivo.write("Notas: " + ", ".join(map(str, notas)) + "\n")
        archivo.write(f"Promedio: {promedioEstudiante}\n\n")
        
        print("Datos guardados en el archivo 'notas.txt'.")
def main():
    presentación()
    ingresoDatos()

#Bloque Principal
main()
