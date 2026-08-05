# Generador de Cuestionarios Interactivo
from utils import *



def main():
   anteriores=[]

   
   data= cargar_preguntas("preguntas_cultura_general.json")
   
   print("\n\tBIENVENIDO AL CUESTIONARIO\n")
   
   while True:
    print(""" \t\t ------ MENU ------
            
        \t  1 - Empezar cuestionario
        \t  2 - Ranking 
        \t  3 - Salir
            
    """)
    opcion= input("Introduce una opcion: ")
    if opcion == "1":
        mis_contadores={
            "aciertos":0,
            "fallos":0    
        }

        nombre= (input("Introduce tu nombre: "))
        cantidad_preguntas = 0

        while cantidad_preguntas < 3:
           n_pregunta = validar_numero(anteriores)
           pregunta=data[n_pregunta]

           respuesta= preguntar(n_pregunta,data)

           validacion= corregir(data, n_pregunta, respuesta)
           mis_contadores, cantidad_preguntas= actualizar_contador(mis_contadores, validacion, cantidad_preguntas)
        
        print("\n CUESTIONARIO FINALIZADO \n")
        for elementos,num in mis_contadores.items():
           print(f"{elementos} : {num}")
        
        aciertos= prc_aciertos(mis_contadores, cantidad_preguntas)
        print(f"Porcentaje de aciertos: {aciertos}")
        mensaje = mensaje_final(aciertos)
        print("\n",mensaje)

        guardar_datos(mis_contadores,nombre,aciertos)

        actualizar_ranking(mis_contadores,nombre)
        
       
    elif opcion == "2":
        puesto=1
        primeros_tres= extraer_ranking()
        print("---- RANKING ----")
        for n,v in primeros_tres.items():
            print(f"{puesto}. {n} : {v:.2f} % de aciertos")
            puesto+=1  


    elif opcion == "3":
        print("Hasta la proxima!")
        break

    
    else:
        print("Por favor, introduce una opcion valida:\n")
       


if __name__=="__main__":
    main()