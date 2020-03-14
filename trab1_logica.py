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

#NOME DA FUNCAO PRECISA MELHORAR
def lista_indices(formula):
    i = 0
    abre = []
    lsub = []
    while i < len(formula):
        if (formula[i] == '('):
            abre.append(i)
        elif (formula[i] == ')'):                        
            inicio = abre.pop()
            if (formula[inicio-1] == conectivos[3]):
                adicionar = formula[inicio-1:i+1]
                if not (adicionar in lsub):
                    lsub.append(formula[inicio-1:i+1])
            adicionar = formula[inicio:i+1]
            if not (adicionar in lsub):
                lsub.append(formula[inicio:i+1])
        i += 1
    return lsub

# VERIFICA SE E FORMULA OU NAO
def isFormula(formula):    
    if ((len(formula) == 1) and (formula in alfabeto)):
        return True #E formula
    elif (formula[0] in conectivos[:3]):
        return False #Nao e formula
    elif 1<len(formula)<3:
        if (formula[0] == conectivos[3] and formula[1] in alfabeto):
            return True #E formula
    elif (len(formula) > 2):
        i = 0
        while i < len(formula)-1:
            if  verificaConectivo(formula[i], formula[i+1]) :
                pass
            elif verificaAtomo(formula[i], formula[i+1]):
                pass
            elif verificaFechaParenteses(formula[i], formula[i+1]):
                pass
            else:
                return False #"Nao e formula"
            i += 1
        return True #"E formula"
    return False #"Nao e formula"

conec1 = [conectivos[3]]
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


def lista_atomos(formula):
    i = 1
    latomos = []
    while (i<len(formula)):
        if((formula[i-1] == conectivos[3]) and (formula[i] in alfabeto)):            
            latomos.append(formula[i-1] + formula[i])            
        if (formula[i] in alfabeto):
            if not (formula[i] in latomos):
                latomos.append(formula[i])
        i += 1
    return latomos

## LISTA PARA CASO DE TESTE
lista = ['((p|q)>(~q&~p))', '(pq)&~(p|q)', 'p', '~p|q', '~(p&q)', '(~(p|q)>(~q&~p)&(p>~(p>(p|q))))']

for a in lista:
    print("ENTRADA: ", a)
    if(isFormula(a)):
        print("E formula")
        print("")
        print("SAIDA: ")
        lista_sub = lista_indices(a)
        lista_sub = lista_atomos(a) + lista_sub
        for i in lista_sub:
            print(i)
        print("")
    else:
        print("Nao e formula")
        print("")