
from first import computeAllFirsts
from follow import computeAllFollows
from axioma_inaccesible import verificar_axioma_inaccesible
from producion_innecesaria import verificar_produccion_innecesaria
from terminales_no_generativos import terminales_no_gen
from select_1 import compute_selects

class _Solucion:
    def setear(self, gramatica):
        self.reglas = {}
        self.nuevas_reglas = {}
        self.EsLL1 = True
        self.first = {}
        self.follows = {}
        self.selects = {}

        #Traducimos la gramatica a un diccionario con el siguiente formato:
        # {'(antecedente)' : ['(consecuente 1)', '(consecuente 2)', ...]}
        lines = gramatica.strip().split("\n")
        for line in lines:
            lhs, rhs = line.split(":")
            rhs = rhs.strip().split()
            if lhs not in self.reglas:
                self.reglas[lhs] = []
            self.reglas[lhs].append(rhs)
        
        print("----------------------Gramática:---------------------------------")
        print(self.reglas)
        print("-----------------------------------------------------------------")
        
        nuevas_reglas = verificar_produccion_innecesaria(self.reglas)
        nuevas_reglas = verificar_axioma_inaccesible(nuevas_reglas)
        nuevas_reglas = terminales_no_gen(nuevas_reglas)

        print("----------------------Gramatica Limpia:---------------------------------")
        print(nuevas_reglas)
        print("-----------------------------------------------------------------")
        # Calculamos los conjuntos First y Follow
        self.firsts = computeAllFirsts(nuevas_reglas)
        self.follows = computeAllFollows("S", nuevas_reglas)
        self.selects = compute_selects(self.firsts, self.follows)

        # Imprimir los conjuntos First, Follow y Select de manera ordenada
        for no_terminal, producciones in self.reglas.items():
            for produccion in producciones:
                produccion_str = " ".join(produccion)
                first_conjunto = set()
                for regla, first in self.firsts.get(no_terminal, []):
                    if list(produccion) == regla:
                        first_conjunto = first
                        break
                select_conjunto = set()
                for regla, select in self.selects.get(no_terminal, []):
                    if list(produccion) == regla:
                        select_conjunto = select
                        break
                follow_conjunto = self.follows.get(no_terminal, set())
                print(f"{no_terminal} : {produccion_str}  First[{', '.join(first_conjunto)}]  Select[{', '.join(select_conjunto)}]  Follow[{', '.join(follow_conjunto)}]")

        self.EsLL1 = self.verificar_LL1()

        
    def obtener_producciones_posibles(self, gramatica, first_sets, select_sets, X, a):
        producciones_posibles = []
        if X in gramatica:
            # Iterar sobre las producciones del no terminal X
            for produccion in gramatica[X]:
                # Verificar en los select_sets si hay una coincidencia para la producción actual
                select_list = select_sets.get(X, [])
                for regla, select in select_list:
                    # Si la regla en select_sets coincide con la producción y contiene 'a' en el conjunto de select
                    if list(produccion) == regla and a in select:
                        producciones_posibles.append(produccion)
                        break  # Encontramos una producción válida, no es necesario seguir buscando
        return producciones_posibles

    def verificar_LL1(self):
        for no_terminal, producciones in self.selects.items():
            select_sets = []
            for _, select in producciones:
                for s in select:
                    if s in select_sets:
                        return False
                    select_sets.append(s)
        return True


    def evaluar_cadena(self, cadena):
        if self.EsLL1:  # Usar el atributo que indica si la gramática es LL(1)
            pila = ["$", next(iter(self.reglas))]  # Asumiendo que `self.gramatica` es el diccionario de gramática
            entrada = cadena + "$"
            indice_entrada = 0
            cadena_valida = True

            while pila:
                X = pila.pop()

                if X == '#':
                    continue

                if indice_entrada < len(entrada):
                    a = entrada[indice_entrada]
                else:
                    print("Error Inesperado")
                    cadena_valida = False
                    break  # Detener la evaluación si la cadena se termina inesperadamente

                if X[0].islower() or X == "$":
                    if X == a:
                        indice_entrada += 1
                    else:
                        cadena_valida = False
                        self.EsLL1 = False
                        break  # Detener la evaluación si no coincide
                else:
                    # Usar la función para obtener las producciones posibles
                    producciones_posibles = self.obtener_producciones_posibles(self.reglas, self.first, self.selects, X, a)

                    if not producciones_posibles:
                        cadena_valida = False
                        self.EsLL1 = False
                        break  # Detener la evaluación si no hay producciones

                    if producciones_posibles:
                        produccion = producciones_posibles[0]
                        nueva_produccion = produccion[::-1]  # Invertir la producción para empujarla a la pila en el orden correcto
                        pila.extend(nueva_produccion)
            if (self.EsLL1):
                print("La gramática es LL")
            else:
                print("La gramática no es LL")

        else:
            print("La gramática no es LL(1)")
            cadena_valida = False
            self.EsLL1 = False
        return cadena_valida