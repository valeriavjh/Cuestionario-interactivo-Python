import json
import random


# Cargar el archivo de preguntas json
def cargar_preguntas(documento):
    with open(documento, 'r', encoding='utf-8') as archivo:
        data = json.load(archivo)
        return data


# Generar un numero aleatorio de pregunta que no haya salido antes
def validar_numero(lista, data):
    while True:
        # Se adapta automáticamente a la cantidad de preguntas que haya en el json
        numero = random.randint(0, len(data) - 1)
        if numero in lista:
            continue
        else:
            lista.append(numero)
            break
    return numero


# Mostrar la pregunta con opciones y recibir el input del usuario
def preguntar(numero, data):
    print("\n", data[numero]["pregunta"], "\n")
    for opciones in data[numero]["opciones"]:
        print(opciones)
    respuesta = input("Elige una opción: (A/B/C/D): ")

    while respuesta.upper() not in ["A", "B", "C", "D"]:
        respuesta = input("Por favor elije una opción. (A / B / C / D): ")
    return respuesta


# Corregir respuesta
def corregir(data, numero, respuesta):
    if respuesta.upper() == data[numero]["respuesta_correcta"]:
        return True
    else:
        return False


def actualizar_contador(contador, respuesta, preguntas):
    """
    Funcion que recibe el parametro "respuesta" y actualiza el diccionario con los contadores
    """
    if respuesta == True:
        contador["aciertos"] += 1
        print("\n¡Respuesta correcta!\n")
    else:
        contador["fallos"] += 1 
        print("\nRespuesta incorrecta.\n")
    
    preguntas += 1   

    return contador, preguntas 


# Porcentaje de aciertos
def prc_aciertos(contador, cantidad_preguntas):
    prc_aciertos = (contador["aciertos"] / cantidad_preguntas) * 100
    return prc_aciertos


# Mensaje al usuario, según el % de aciertos
def mensaje_final(porcentaje):
    if porcentaje >= 80:
        return "\n¡Te has pasado el juego, enhorabuena!\n"
    if porcentaje >= 50:
        return "\n¡Buen trabajo! Con un cafe más dominas el mundo\n"
    else:
        return "\nTe toca repasar un poco. Mejor suerte para la proxima\n"


def guardar_datos(contador, usuario, porcentaje):
    """
    Recibe datos generados en el cuestionario y actualiza el diccionario
    """
    contador.clear()
    contador.update({usuario: porcentaje})


"""
===============================================================================================
GUARDAR DATOS EN JSON
=============================================================================================
"""
def actualizar_ranking(contador, usuario):
    # Abrimos el archivo de ranking
    with open("ranking.json", 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)

    
    if usuario in datos:
        if contador[usuario] > datos[usuario]:
            datos[usuario] = contador[usuario]
    else:        
        datos.update(contador)

    # Guardar los cambios en el archivo
    with open("ranking.json", 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


"""
===============================================================================================
Mostrar Ranking
=============================================================================================
"""
def extraer_ranking():
    with open("ranking.json", 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
        
    dict_ordenado = dict(sorted(datos.items(), key=lambda item: item[1], reverse=True))
    primeros_tres = dict(list(dict_ordenado.items())[:3])

    return primeros_tres
