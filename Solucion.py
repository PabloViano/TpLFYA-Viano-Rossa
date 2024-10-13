
from first import computeAllFirsts
from follow import computeAllFollows

def main():
    gramatica = "S:Q a\nS:P\nQ:c\nP:P x"
    reglas = {}
    lines = gramatica.strip().split("\n")
    for line in lines:
        # Dividir la producción en lado izquierdo (no terminal) y derecho (producción)
        lhs, rhs = line.split(":")
        rhs = rhs.strip().split()  # Dividir la producción en símbolos

        # Agregar la producción al diccionario de reglas
        if lhs not in reglas:
            reglas[lhs] = []
        reglas[lhs].append(rhs)
    
    print("Gramática:")
    print(reglas)

    # Calculamos los conjuntos First y Follow
    firsts = computeAllFirsts(reglas)
    follows = computeAllFollows("S", reglas)

    print("Conjuntos First:")
    for no_terminal, conjunto in firsts.items():
        print(f"{no_terminal}: {conjunto}")
    
    print("\nConjuntos Follow:")
    for no_terminal, conjunto in follows.items():
        print(f"{no_terminal}: {conjunto}")

if __name__ == "__main__":
    main()