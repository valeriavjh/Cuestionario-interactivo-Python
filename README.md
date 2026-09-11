# Generador de Cuestionarios Interactivo

Aplicación de consola en Python desarrollada como proyecto práctico para el módulo profesional optativo. Permite realizar cuestionarios tipo test de cultura general, validar respuestas en tiempo real, calcular estadísticas de aciertos y registrar las mejores puntuaciones en un ranking persistente.

---

## 🚀 Características

* **Menú interactivo:** Menú cíclico por consola con opciones para iniciar partida, consultar el ranking o salir del programa.
* **Partidas personalizadas:** El usuario introduce su nombre y elige cuántas preguntas desea responder en cada intento.
* **Preguntas aleatorias sin repetición:** Las preguntas se cargan desde un archivo JSON externo y se seleccionan al azar sin duplicarse durante la partida.
* **Validación en tiempo real:** Aviso instantáneo tras responder que indica si la opción elegida fue correcta o incorrecta.
* **Estadísticas finales:** Desglose con el total de aciertos, fallos, porcentaje de éxito y un mensaje personalizado según la puntuación obtenida.
* **Sistema de Ranking:** Registro persistente en JSON que guarda únicamente la mejor puntuación de cada jugador y muestra el Top 3.

---

## 📁 Estructura del proyecto

```text
├── cuestionario_interactivo.py       # Archivo principal (flujo del programa y menú)
├── utils.py                          # Módulo con funciones lógicas, validaciones y ficheros
├── preguntas_cultura_general.json    # Banco de preguntas y respuestas en formato JSON
├── ranking.json                      # Base de datos persistente con las puntuaciones récord
└── README.md                         # Documentación del proyecto
