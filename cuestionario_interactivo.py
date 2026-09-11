# Generador de Cuestionarios Interactivo
from utils import *


def main():
    data = cargar_preguntas("preguntas_cultura_general.json")
   
    print("\n\tBIENVENIDO AL CUESTIONARIO\n")
   
    while True:
        print(""" \t\t ------ MENU ------
            
        \t  1 - Empezar cuestionario
        \t  2 - Ranking 
        \t  3 - Salir
            
        """)
        opcion = input("Introduce una opcion: ")
        
        if opcion == "1":
        
            anteriores = []

            mis_contadores = {
                "aciertos": 0,
                "fallos": 0    
            }

            nombre = input("Introduce tu nombre: ")

            # NUEVO: Pedir cuántas preguntas quiere responder el usuario
            max_posibles = len(data)
            while True:
                total_deseado = input(f"¿Cuántas preguntas quieres responder? (1 a {max_posibles}): ")
                if total_deseado.isdigit():
                    total_deseado = int(total_deseado)
                    if 1 <= total_deseado <= max_posibles:
                        break
                    else:
                        print(f"Por favor, elige un número entre 1 y {max_posibles}.")
                else:
                    print("Introduce un número válido.")

            cantidad_preguntas = 0

            # El bucle ahora se repite hasta alcanzar el número elegido
            while cantidad_preguntas < total_deseado:
                n_pregunta = validar_numero(anteriores, data)
                pregunta = data[n_pregunta]

                respuesta = preguntar(n_pregunta, data)

                validacion = corregir(data, n_pregunta, respuesta)
                mis_contadores, cantidad_preguntas = actualizar_contador(mis_contadores, validacion, cantidad_preguntas)
            
            print("\n CUESTIONARIO FINALIZADO \n")
            for elementos, num in mis_contadores.items():
                print(f"{elementos} : {num}")
            
            aciertos = prc_aciertos(mis_contadores, cantidad_preguntas)
            print(f"Porcentaje de aciertos: {aciertos:.2f}%")
            mensaje = mensaje_final(aciertos)
            print("\n", mensaje)

            guardar_datos(mis_contadores, nombre, aciertos)

            actualizar_ranking(mis_contadores, nombre)
            
        elif opcion == "2":
            puesto = 1
            primeros_tres = extraer_ranking()
            print("---- RANKING ----")
            for n, v in primeros_tres.items():
                print(f"{puesto}. {n} : {v:.2f} % de aciertos")
                puesto += 1  

        elif opcion == "3":
            print("Hasta la proxima!\n")
            break
        
        else:
            print("Por favor, introduce una opcion valida:\n")


if __name__ == "__main__":
    main()