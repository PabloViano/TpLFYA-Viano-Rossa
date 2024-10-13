def verificar_produccion_innecesaria(reglas):
    for ant, cons in reglas.items():
                for produccion in cons:
                        if len(produccion) == 1:  # Iteramos sobre cada producción
                            if produccion[0] == ant:
                                reglas[ant].remove(produccion)
    return reglas  # Devolvemos las reglas limpias