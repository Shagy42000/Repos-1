import random

# Definir parámetros
ciudades = ["Loja", "Ibarra", "Ambato"]  # Tres ciudades como ejemplo
dias_de_la_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Número de semanas

# Inicializar la matriz 3D con temperaturas aleatorias entre 10 y 35 grados Celsius
matriz_temperaturas = [[[random.randint(10, 35) for _ in range(len(dias_de_la_semana))] for _ in range(semanas)] for _ in range(len(ciudades))]

# Mostrar las temperaturas (opcional, para verificar)
print("Matriz de temperaturas:")
for i, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    for j in range(semanas):
        print(f"Semana {j + 1}: {matriz_temperaturas[i][j]}")

# Calcular y mostrar los promedios por ciudad y semana
print("\nPromedios de temperaturas por ciudad y semana:")
for i, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    for j in range(semanas):
        promedio = sum(matriz_temperaturas[i][j]) / len(dias_de_la_semana)
        print(f"Semana {j + 1}: {promedio:.2f} °C")
