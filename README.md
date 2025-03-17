# Optimización de Estaciones de Radio

## Explicación del problema
El problema consiste en encontrar la combinación más pequeña de estaciones de radio (13) para que se escuche a Beyoncé en todos los estados (22). Nuestro objetivo es seleccionar una combinación óptima que garantice la cobertura total con la menor cantidad de estaciones.


## Solución encontrada
Se han implementado dos enfoques heurísticos para abordar el problema:

1. **Búsqueda  Global**
   - Se selecciona iterativamente la estación que cubre la mayor cantidad de estados restantes.
   - Se repite este proceso hasta que todos los estados estén cubiertos.
   - Es una solución rápida y simple, pero no garantiza el resultado óptimo.

2. **Búsqueda Local**
   - Se realizan múltiples intentos aleatorios seleccionando estaciones en distintos órdenes.
   - Se compara la cobertura lograda en cada intento y se guarda la mejor solución encontrada.
   - Esto permite mejorar la solución de la búsqueda global al explorar diferentes combinaciones de estaciones.

## Comparación entre búsquedas y optimización

| Método                | Rapidez | Calidad de la solución | Complejidad |
|-----------------------|---------|------------------------|-------------|
| **Búsqueda Global**   | Alta    | Aceptable              | Baja        |
| **Búsqueda Local**    | Media   | Puede ser mejor        | Media       |

La búsqueda global proporciona una solución inicial eficiente, mientras que la búsqueda local intenta optimizar el resultado probando diferentes combinaciones. La calidad de la solución local depende del número de iteraciones realizadas.

## Clonar el repositorio
Para obtener el código, clona el repositorio desde GitHub con los siguientes comandos:

git clone https://github.com/sergiomenurt/Optimizacion-estaciones-radio.git
cd Optimizacion-estaciones-radio

## Ejecución
Para ejecutar el código en Python, usa el siguiente comando en la terminal:

python busqueda_estaciones_radio.py

## Asegúrate de tener Python instalado para poder ejecutar el script correctamente.
