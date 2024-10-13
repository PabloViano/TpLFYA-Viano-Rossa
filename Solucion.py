
from first import computeAllFirsts
from follow import computeAllFollows
from axioma_inaccesible import verificar_axioma_inaccesible
from producion_innecesaria import verificar_produccion_innecesaria

{
    "S" : [["X", "Y", "Z"]],
    "X" : [["a", "X"], ["#"]],
}
def main():
    gramatica = "S:Q a\nS:P\nP:b\nQ:b\nQ:lambda"
    reglas = {}
    nuevas_reglas = {}

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
    
    #Verificar Produccion innecesaria
    nuevas_reglas = verificar_produccion_innecesaria(reglas)

    #Verificar que el antecedente sea accesible desde el axioma
    nuevas_reglas = verificar_axioma_inaccesible(reglas)
    print("Gramtica limpia:")
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

    print("\nConjunto Selects:")

if __name__ == "__main__":
    main()