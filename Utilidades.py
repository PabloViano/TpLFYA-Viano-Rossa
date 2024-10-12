class Utilidades:
    
    def primera_letra(regla,terminal,primer_variable):
        listadoFirsts = set()
        char = ''
        for i in range(len(regla)):
            char_ = regla[i]
            char = char + regla[i]
            if(char_.isupper()):
                char = ''
                listadoFirsts = listadoFirsts.union(primer_variable[char_])
                if ('lambda' in primer_variable[char_]) and (i!=len(regla)-1):
                    listadoFirsts = listadoFirsts - {'lambda'}
                else:
                    break
            else:
                if char in terminal:
                    set_terminal = set([char])
                    listadoFirsts = listadoFirsts.union(set_terminal)
                    break
        return listadoFirsts