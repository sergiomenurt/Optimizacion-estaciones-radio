import random

# Código del algoritmo de busqueda global
def busqueda_avida_global(estaciones, estados_necesarios):
    """ Búsqueda Ávida Global: Selecciona siempre la estación con mayor cobertura. """
    estaciones_seleccionadas = set()
    while estados_necesarios:
        mejor_estacion = max(estaciones, key=lambda e: len(estaciones[e] & estados_necesarios), default=None)
        if not mejor_estacion:
            break
        estaciones_seleccionadas.add(mejor_estacion)
        estados_necesarios -= estaciones[mejor_estacion]
    return estaciones_seleccionadas

# Código del algoritmo de busqueda local
def busqueda_avida_local(estaciones, estados_necesarios, iteraciones=100):
    """ Búsqueda Ávida Local: Realiza múltiples intentos aleatorios y guarda la mejor solución. """
    mejor_solucion = None
    for _ in range(iteraciones):
        estaciones_seleccionadas, estados_restantes = set(), estados_necesarios.copy()
        for estacion in random.sample(list(estaciones.keys()), len(estaciones)):
            if estados_restantes & estaciones[estacion]:
                estaciones_seleccionadas.add(estacion)
                estados_restantes -= estaciones[estacion]
        if mejor_solucion is None or len(estaciones_seleccionadas) < len(mejor_solucion):
            mejor_solucion = estaciones_seleccionadas
    return mejor_solucion

# Lista de las 13 estaciones
estaciones = {
    "kone": {"ID", "NV", "UT"}, "ktwo": {"WA", "ID", "MT"}, "kthree": {"OR", "NV", "CA"},
    "kfour": {"NV", "UT"}, "kfive": {"CA", "AZ"}, "ksix": {"NM", "TX", "OK"},
    "ksiete": {"OK", "KS", "CO"}, "kocho": {"KS", "CO", "NE"}, "knueve": {"NE", "SD", "WY"},
    "kdiez": {"ND", "IA"}, "konce": {"MN", "MO", "AR"}, "kdoce": {"LA"}, "ktrece": {"MO", "AR"}
}

estados_necesarios = set.union(*estaciones.values())

# Ejecutar ambos algoritmos
resultado_global = busqueda_avida_global(estaciones, estados_necesarios)
resultado_local = busqueda_avida_local(estaciones, estados_necesarios)

# Mostrar por pantalla los resultados
print("\nBúsqueda Ávida Global - Estaciones seleccionadas:", resultado_global)
print("\nBúsqueda Ávida Local - Estaciones seleccionadas:", resultado_local)
