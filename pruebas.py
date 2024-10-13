#gramatica = "S:a Q\nQ:b R\nQ:c R\nR:R d"
#reglas = {}
#reglas = gramatica.split("\n")
#newReglas = {}
#for regla in reglas:
#    ant, con = regla.split(":")
#    print("Antecedente: ", ant , "Consecuente: ", con)

from Utilidades import Utilidades

production = {'S': ['a Q', 'R b'], 'Q': ['b S', 'c R'], 'R': ['S d','lambda']
}
#production = {'S': ['X Y Z'], 'X': ['a', 'b', 'lambda'], 'Y': ['a','d','lambda'], 'Z': ['e', 'f', 'lambda']}

terminal = {'a', 'b', 'c','d','lambda'}


def BuscarFirst(noTerminalesConSusReglas, terminales):
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
                            if ('^' in Response[char_]) and (x != Longitud-1):
                                tmp_set = tmp_set - {'^'}
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

print("First")
print(BuscarFirst(production, terminal))


def BuscarFollows(production,terminal,start_symbol,first_of_variables):
	ans = dict()
	for var in production:
		ans[var] = set()
	#ans[start_symbol] = {'$'}
	change = 1
	while change:
		change = 0
		for var in production:
			tmp_set = ans[var]
			if(var == start_symbol):
				tmp_set = tmp_set.union({'$'})
			for lhs in production:
				for p in production[lhs]:
					if p.find(var)<0:
						continue
					elif p.find(var)<len(p)-1:
						alpha = p[p.find(var)+1]
						#print(var + " " + alpha)
						if '^' not in Utilidades.primera_letra(alpha,terminal,first_of_variables):
							tmp_set = tmp_set.union(Utilidades.primera_letra(alpha,terminal,first_of_variables))
						else:
							tmp_set = tmp_set.union(Utilidades.primera_letra(alpha,terminal,first_of_variables))
							tmp_set = tmp_set - {'^'}
							tmp_set = tmp_set.union(ans[lhs])
					else:
						tmp_set = tmp_set.union(ans[lhs])
			if tmp_set != ans[var]:
				ans[var] = tmp_set
				change = 1
	return ans

print("Follows")
print(BuscarFollows(production, terminal, 'S', BuscarFirst(production, terminal)))


def BuscarSelects(firstReglas):
    for i in firstReglas:
        if 'lambda' in firstReglas[i]:
            firstReglas[i].remove('lambda')
    return firstReglas

print("Selects")
print(BuscarSelects(BuscarFirst(production, terminal)))