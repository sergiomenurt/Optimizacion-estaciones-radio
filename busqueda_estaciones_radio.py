import random

def busqueda_avida_global(estaciones, estados_necesarios):
    """ Búsqueda Ávida Global: Selecciona siempre la estación con mayor cobertura. """
    estaciones_seleccionadas = set()
    estados_restantes = estados_necesarios.copy() 
    
    while estados_restantes:
        mejor_estacion = max(estaciones, key=lambda e: len(estaciones[e] & estados_restantes), default=None)
        if not mejor_estacion:
            break
        estaciones_seleccionadas.add(mejor_estacion)
        estados_restantes -= estaciones[mejor_estacion]
    
    return estaciones_seleccionadas

def busqueda_avida_local(estaciones, estados_necesarios, iteraciones=100):
    """ Búsqueda Ávida Local: Realiza múltiples intentos aleatorios y guarda la mejor solución. """
    mejor_solucion = busqueda_avida_global(estaciones, estados_necesarios)  # Solución inicial válida
    
    for _ in range(iteraciones):
        estaciones_seleccionadas = set()
        estados_restantes = estados_necesarios.copy()  # Asegurar que se reinicia en cada intento
        
        # Empezamos seleccionando estaciones de forma aleatoria
        estaciones_aleatorias = random.sample(list(estaciones.keys()), len(estaciones))
        
        while estados_restantes:
            # Se elige aleatoriamente una estación que cubra los estados restantes
            estaciones_posibles = [estacion for estacion in estaciones_aleatorias if estados_restantes & estaciones[estacion]]
            
            if not estaciones_posibles:
                break
            
            estacion_elegida = random.choice(estaciones_posibles)  # Elegir una estación aleatoria entre las posibles
            estaciones_seleccionadas.add(estacion_elegida)
            estados_restantes -= estaciones[estacion_elegida]  # Restar los estados cubiertos
        
        # Guardar solo si cubre todos los estados y usa menos estaciones
        if not estados_restantes and len(estaciones_seleccionadas) < len(mejor_solucion):
            mejor_solucion = estaciones_seleccionadas
    
    return mejor_solucion

# Definir estaciones y estados cubiertos
estaciones = {
    "kone": {"ID", "NV", "UT"}, "ktwo": {"WA", "ID", "MT"}, "kthree": {"OR", "NV", "CA"},
    "kfour": {"NV", "UT"}, "kfive": {"CA", "AZ"}, "ksix": {"NM", "TX", "OK"},
    "ksiete": {"OK", "KS", "CO"}, "kocho": {"KS", "CO", "NE"}, "knueve": {"NE", "SD", "WY"},
    "kdiez": {"ND", "IA"}, "konce": {"MN", "MO", "AR"}, "kdoce": {"LA"}, "ktrece": {"MO", "AR"}
}

estados_necesarios = set.union(*estaciones.values())

# Ejecutar algoritmos
resultado_global = busqueda_avida_global(estaciones, estados_necesarios)
resultado_local = busqueda_avida_local(estaciones, estados_necesarios)

print("\nBúsqueda Ávida Global - Estaciones seleccionadas:", resultado_global)
print("\nBúsqueda Ávida Local - Estaciones seleccionadas:", resultado_local)
