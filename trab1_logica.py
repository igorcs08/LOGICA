lista_sub = []

alfabeto = ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
conectivos = ['&', '|', '>', '~']
auxiliares = ['(', ')']

#SO IDENTIFICA A QUANTIDADE
def qnt_parenteses(formula):
    cont = 0
    for atomo in formula:
        if atomo == '(':
            cont = cont + 1
        elif atomo == ")":
            cont = cont - 1 
    if cont == 0 :
        return True
    else:
        return False

# INDICE DE CADA PARENTESES
def lista_indices(formula):
    i = 0
    indices = []
    while i < len(formula):        
        if(formula[i] == '(' or formula[i] == ')'):
            indices.append(i)
        i += 1
    return indices

# VERIFICA SE E FORMULA OU NAO
def isFormula(formula):    
    if ((len(formula) == 1) and (formula in alfabeto)):
        return "E formula"
    elif (formula[0] in conectivos[:3]):
        return "Nao e formula"
    elif (len(formula) > 1):
        i = 0
        while i < len(formula)-1:
            if  verificaConectivo(formula[i], formula[i+1]) :
                pass
            elif verificaAtomo(formula[i], formula[i+1]):
                pass
            elif verificaFechaParenteses(formula[i], formula[i+1]):
                pass
            else:
                return "Nao e formula"
            i += 1
        return "E formula"
    return "Nao e formula"

conec1 = conectivos[3:5]
co = [auxiliares[0]]+conectivos
conec1 += alfabeto
conec1.append(auxiliares[0])

def verificaConectivo(atomo, atomo2):
    #print([atomo, atomo2])
    #print("aqui1")
    #print(co)    
    #print(conec1)
    if (atomo in co):
        #print("aqui1----1")
        if (atomo2 in conec1):
            #print("aqui1----2")
            return True        
        return False
    return False

conec2 = conectivos[:3]+[auxiliares[1]]

def verificaFechaParenteses(atomo, atomo2):
    #print([atomo, atomo2])
    #print("aqui3")
    if (atomo == ')'):
        #print("aqui3----1")
        if (atomo2 in conec2):
            #print("aqui3----2")
            if not((atomo == ")" and atomo2 == "(")):
                #print("aqui3----3")
                return True
            return False
        return False
    return False


conec = conectivos
conec.append(auxiliares[1])

def verificaAtomo(atomo, atomo2):
    #print([atomo, atomo2])
    #print("aqui2")
    if (atomo in alfabeto):
        #print("aqui2----1")
        if (atomo2 in conec):
            #print("aqui2----2")
            if not ((atomo in alfabeto) and (atomo2 == "~")):
                #print("aqui2----3")
                return True
            return False
        return False
    return False

"""
def separa(formula):
    ind = lista_indices(formula)
    for i in ind:
"""        

"""
def separa(formula):
    ind = lista_indices(formula)
    while i < len(formula):
        if formula[i] and fo
"""

def separa(formula):
    lista_sub.append(formula)
    if (formula[0] == '(' and formula[-1] == ')'):
        if (formula[1] == '(' and formula[-2] == ')'):
            formula = formula[1:-1]
    indexes = lista_indices(formula)
    i = 0
    j = len(indexes)
    while (i < j):
        print(j)
        i = 0
        print(len(indexes))
        lista_sub.append(formula[indexes[i]:indexes[i+1]])
        indexes.pop(0)
        indexes.pop(1)
        j = len(indexes)
        i += 1


a = "(p|q)>(~q&~p)"
#a = "p|~q"
print(a)

print(isFormula(a))
separa(a)
print(lista_sub)
    