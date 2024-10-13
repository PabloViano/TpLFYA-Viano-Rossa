
def compute_selects(first_dict, follow_dict):
    selects = {}
    # Recorremos cada no terminal y sus respectivas producciones en first_dict
    for lhs, productions in first_dict.items():
        select_list = []
        for consequent, first_set in productions:
            select_set = first_set.copy()
            # Si "λ" está presente en el conjunto First, lo eliminamos
            if "#" in select_set:
                select_set.remove("#")
                # Agregamos el conjunto Follow del no terminal al conjunto Select
                select_set.update(follow_dict.get(lhs, set()))
            # Añadimos el conjunto Select para el consecuente actual
            select_list.append((consequent, select_set))
        selects[lhs] = select_list
    return selects