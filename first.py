#verificar que sea terminal
def is_terminal(char):
    return not char.isupper()

#verificar que el caracter es no terminal
def is_non_terminal(char):
    return char.isupper()

#Calcular conjunto de First. Rule (regla representada en una lista) Prods (gramatica en diccionario)
def first(rule, prods):
    #Verifico que no sea vacio
    if len(rule) != 0 and (rule is not None):
        #Es terminal lo retorno
        if is_terminal(rule[0]):
            return rule[0]
        #Es lambda lo retorno
        elif rule[0] == "#":
            return "#"

    if len(rule) != 0:
        #Si es un no terminal calculo su first
        if rule[0] in list(prods.keys()):
            fres = []
            rhs_rules = prods[rule[0]]
            for itr in rhs_rules:
                indivRes = first(itr, prods)
                if type(indivRes) is list:
                    for i in indivRes:
                        fres.append(i)
                else:
                    fres.append(indivRes)
            #Si no puede derivar en lambda lo retorno
            if "#" not in fres:
                return fres
            #Sino sigo calculando
            else:
                newList = []
                fres.remove("#")
                if len(rule) > 1:
                    ansNew = first(rule[1:], prods)
                    if ansNew != None:
                        if type(ansNew) is list:
                            newList = fres + ansNew
                        else:
                            newList = fres + [ansNew]
                    else:
                        newList = fres
                    return newList
                fres.append("#")
                return fres

#Calculo los first para todos los no terminales (prods es un diccionario key: no terminal, value: reglas)
def computeAllFirsts(prods):
    #Creo un diccionario para guardar los first
    first_set={}
    #Recorro todos los no terminales y le calculo su first
    for lhs in list(prods.keys()):
        temp = set()
        for sub in prods.get(lhs):
            res = first(sub, prods)
            if res != None:
                if type(res) is list:
                    for u in res:
                        temp.add(u)
                else:
                    temp.add(res)
        #Almaceno el conjunto de first para el no terminal
        first_set[lhs] = temp

    #Diccionario con cada terminal y su conjunto de first
    return first_set
