from first import is_non_terminal

def terminales_no_gen(gramatica):
    generativos = set()

    algo_nuevo = True
    while algo_nuevo:
        algo_nuevo = False
        for ant, cons in gramatica.items():
            if ant not in generativos:
                for produccion in cons: #Recorremos cada regla
                    # Verificamos si todos los elementos de la producción son generativos o terminales
                    cc_gen = all(c in generativos or not is_non_terminal(c) for c in produccion)
                    
                    if cc_gen:  # Si la producción es completamente generativa
                        algo_nuevo = True
                        generativos.add(ant)
                        break 

    # Filtramos las reglas para mantener solo las que tienen no terminales generativos
    n_reglas = {}
    for ant, cons in gramatica.items():
        if ant in generativos:
            # Agregamos solo las producciones que consisten en símbolos generativos
            n_reglas[ant] = [prod for prod in cons if all(c in generativos or not is_non_terminal(c) for c in prod)]

    return n_reglas
