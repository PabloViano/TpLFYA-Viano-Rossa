
from first import computeAllFirsts
from follow import computeAllFollows
from axioma_inaccesible import verificar_axioma_inaccesible
from producion_innecesaria import verificar_produccion_innecesaria
from terminales_no_generativos import terminales_no_gen
from select_1 import compute_selects

class _Solucion:
    def setear(self, gramatica):
        reglas = {}
        nuevas_reglas = {}

        #Traducimos la gramatica a un diccionario con el siguiente formato:
        # {'(antecedente)' : ['(consecuente 1)', '(consecuente 2)', ...]}
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
        nuevas_reglas = verificar_axioma_inaccesible(nuevas_reglas)

        #Verificar terminales no generativos
        nuevas_reglas = terminales_no_gen(nuevas_reglas)

        # Calculamos los conjuntos First y Follow
        firsts = computeAllFirsts(nuevas_reglas)
        follows = computeAllFollows("S", nuevas_reglas)
        selects = compute_selects(firsts, follows)

        print("Conjuntos First:")
        print(firsts)
        
        print("\nConjuntos Follow:")
        print(follows)

        print("\nConjunto Selects:")
        print(selects)

    def evaluar_cadena(self, cadena):
        pass