from calificaciones import *

data = pedir_datos()
print("Aciertos: " + data[0] + "\nErrores: " + data[1] + "\nRespuestas totales: " + data[2])

print("Nota del alumno: " + calculadora(data[0], data[1], data[2]))