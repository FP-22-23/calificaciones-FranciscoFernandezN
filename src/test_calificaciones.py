from calificaciones import *

def main():
    """aciertos, errores, total_respuestas = pedir_datos()
    nota = calculadora(aciertos, errores, total_respuestas)
    print("Tu nota es " + str(nota))"""

    cuestionarios = pide_cuestionarios()
    parciales = pide_parciales()
    proyectos = pide_proyectos()

    nota_evaluacion = calcula_nota_evaluacion_continua(cuestionarios, parciales, proyectos)
    print("Tu nota de la evaluación continua es: " + str(nota_evaluacion))

if __name__ == "__main__":
    main()