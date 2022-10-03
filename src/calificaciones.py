def pedir_datos():
    aciertos = int(input("Número de aciertos del alumno: "))
    errores = int(input("Número de errores del alumno: "))
    respuestas = int(input("Número de respuestas totales: "))
    return (aciertos, errores, respuestas)

def calculadora(aciertos, errores, respuestas):
    nota = ((aciertos * 10)/respuestas) - ((errores * 10)/(50 - respuestas))
    return (max([0, nota]))

def pide_cuestionarios():
    lista = []
    for i in range(6):
        lista.append(float(input("Nota del " + str(i+1) + " cuestionario: ")))
    return tuple(lista)

def pide_parciales():
    lista = []
    for i in range(2):
        lista.append(float(input("Nota del " + str(i+1) + " parcial: ")))
    return tuple(lista)

def pide_proyectos():
    lista = []
    for i in range(2):
        lista.append(float(input("Nota del " + str(i+1) + " proyecto: ")))
    return tuple(lista)

def calcula_nota_cuatrimestre(cuestionarios, parcial, proyecto):
    if proyecto < 5:
        return 3
    else:
        nota = 0.1 * (cuestionarios[0] + cuestionarios[1] + cuestionarios[2]) + 0.6 * parcial + 0.1 * proyecto
        return max([0, nota])

def calcula_nota_evaluacion_continua(cuestionarios, parciales, proyectos):
    print(cuestionarios[:3])
    print(cuestionarios[3:6])
    primer_cuatri = calcula_nota_cuatrimestre(cuestionarios[:3], parciales[0], proyectos[0])
    segundo_cuatri = calcula_nota_cuatrimestre(cuestionarios[3:6], parciales[1], proyectos[1])
    if primer_cuatri > 4 and segundo_cuatri > 4:
        return (primer_cuatri + segundo_cuatri)/2
    else:
        return 4