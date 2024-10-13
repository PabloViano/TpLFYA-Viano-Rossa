
def verificar_axioma_inaccesible(reglas):
    accesibles = set(["S"])  # Símbolo inicial accesible
    hay_cambios = True  # Indica si encontramos nuevos símbolos accesibles

    # Bucle para encontrar todos los símbolos accesibles
    while hay_cambios:
        hay_cambios = False
        for ant, cons in reglas.items():
            if ant in accesibles:
                # Verificamos los símbolos en cada consecuencia
                for produccion in cons:  # Iteramos sobre cada producción
                    for simbolo in produccion:  # Iteramos sobre cada símbolo en la producción
                        if simbolo not in accesibles:
                            accesibles.add(simbolo)  # Agregamos el símbolo accesible
                            hay_cambios = True  # Indicamos que hubo un cambio

    # Filtramos las reglas con símbolos accesibles
    reglas_accesibles = {
        ant: cons
        for ant, cons in reglas.items()
        if ant in accesibles and all(all(c in accesibles for c in produccion) for produccion in cons)
    }

    return reglas_accesibles  # Devolvemos las reglas limpias


