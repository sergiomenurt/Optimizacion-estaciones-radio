import random

# Búsqueda global
def busqueda_avida_global(stations, needed_states):
    """ Búsqueda Ávida Global: Selecciona siempre la estación con mayor cobertura. """
    selected_stations = set()
    remaining_states = needed_states.copy()

    while remaining_states:
        best_station = max(stations, key=lambda station: len(stations[station] & remaining_states), default=None)
        if not best_station:
            break
        selected_stations.add(best_station)
        remaining_states -= stations[best_station]

    return selected_stations

# Búsqueda local
def greedy_search_local(stations, needed_states):
    NUM_SEARCHES = 5  # Número de búsquedas locales
    best_solution = None  # Mejor solución encontrada
    best_coverage = 0  # Mejor cobertura encontrada
    
    for _ in range(NUM_SEARCHES):
        covered_states = set()  # Estados cubiertos en este intento
        selected_stations = set()  # Estaciones seleccionadas en este intento
        
        # Selección aleatoria de estaciones
        random_stations = random.sample(list(stations.keys()), len(stations))  # Se seleccionan todas las estaciones
        
        for station in random_stations:
            covered_states |= stations[station]  # Añadir estados cubiertos por la estación seleccionada
            selected_stations.add(station)  # Agregar la estación al conjunto de estaciones seleccionadas
        
        # Verificar cuántos estados están cubiertos
        uncovered_states = len(needed_states - covered_states)
        
        # Guardar la mejor solución si cubre todos los estados
        if uncovered_states == 0 and (best_solution is None or len(selected_stations) < len(best_solution)):
            best_solution = selected_stations
            best_coverage = len(covered_states)
    
    return best_solution, best_coverage

# Lista de estaciones
stations = {
    "kone": {"ID", "NV", "UT"},
    "ktwo": {"WA", "ID", "MT"},
    "kthree": {"OR", "NV", "CA"},
    "kfour": {"NV", "UT"},
    "kfive": {"CA", "AZ"},
    "ksix": {"NM", "TX", "OK"},
    "kseven": {"OK", "KS", "CO"},
    "keight": {"KS", "CO", "NE"},
    "knine": {"NE", "SD", "WY"},
    "kten": {"ND", "IA"},
    "keleven": {"MN", "MO", "AR"},
    "ktwelve": {"LA"},
    "kthirteen": {"MO", "AR"}
}

needed_states = set.union(*stations.values())

# Ejecutar búsqueda global
global_result = busqueda_avida_global(stations, needed_states)

# Ejecutar búsqueda local 
best_solution, best_coverage = greedy_search_local(stations, needed_states)

# Imprimir resultados

print("\nBúsqueda Ávida Global - Estaciones seleccionadas:", global_result)

print("\nBúsqueda Ávida Local Aleatoria - Estaciones seleccionadas:", best_solution)
print("Cobertura de estados:", best_coverage)
