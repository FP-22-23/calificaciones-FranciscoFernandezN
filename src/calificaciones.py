def pedir_datos():
    aciertos = int(input("Número de aciertos del alumno: "))
    errores = int(input("Número de errores del alumno: "))
    respuestas = int(input("Número de respuestas totales: "))
    return (aciertos, errores, respuestas)

def calculadora(aciertos, errores, respuestas):
    nota = ((aciertos * 10)/respuestas) - ((errores * 10)/(50 - respuestas))
    return (max([0, nota]))