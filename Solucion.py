from Utilidades import primera_letra

class Gramatica:

    def __init__(self):
        """
        TODO: Docstrings
        """
        self.EsLL1 = False
        #Diccionario con las reglas de la gramatica
        self.reglas = {}

    def setear(self, gramatica):
        reglas = gramatica.split("\n")
        newReglas = {}

    def BuscarFirsts(noTerminalesConSusReglas, terminales):
        Response = dict()
        for var in noTerminalesConSusReglas:
            Response[var] = set()
        cambio = 1
        while cambio:
            cambio = 0
            for var in noTerminalesConSusReglas:
                tmp_set = Response[var]
                for regla in noTerminalesConSusReglas[var]:
                    Longitud = len(regla)
                    char = ''
                    #Recorrer la regla letra por letra
                    for x in range(Longitud):
                        char_ = regla[x]
                        char = char + regla[x]
                        if (char_.isupper()):
                            char = ''
                            tmp_set = tmp_set.union(Response[char_])
                            if ('lambda' in Response[char_]) and (x != Longitud-1):
                                tmp_set = tmp_set - {'lambda'}
                            else:
                                break
                        else:
                            if (char in terminales):
                                set_terminal = set([char])
                                tmp_set = tmp_set.union(set_terminal)
                                break
                if tmp_set != Response[var]:
                    Response[var] = tmp_set
                    cambio = 1
        return Response

    def BuscarFollows(reglas,terminal,primer_simbolo,primer_variable):
        Response = dict()
        for var in reglas:
            Response[var] = set()
        cambio = 1
        while cambio:
            cambio = 0
            for var in reglas:
                tmp_set = Response[var]
                if (var == primer_simbolo):
                    tmp_set = tmp_set.union({'$'})
                for regla in reglas:
                    for char in reglas[regla]:
                        if char.find(var) < 0:
                            continue
                        elif char.find(var) < len(char)-1:
                            alpha = char[char.find(var)+1]
                            if 'lambda' not in primera_letra(alpha, terminal, primer_variable):
                                tmp_set = tmp_set.union(primera_letra(alpha, terminal, primer_variable))
                            else:
                                tmp_set = tmp_set.union(primera_letra(alpha, terminal, primer_variable))
                                tmp_set = tmp_set - {'lambda'}
                                tmp_set = tmp_set.union(Response[regla])
                        else:
                            tmp_set = tmp_set.union(Response[regla])
                if tmp_set != Response[var]:
                    Response[var] = tmp_set
                    cambio = 1
        return Response

    def BuscarSelects():
        pass