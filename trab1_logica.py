#SO IDENTIFICA A QUANTIDADE
def qnt_parenteses(formula):
    cont = 0
    for atomo in formula:
        if atomo == '(':
            cont = cont + 1
        elif atomo == ")":
            cont = cont - 1
    if cont == 0:
        return True
    else:
        return False

alfabeto = ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
conec = ['&', '|', '>', '~', '(', ')']

def conectivos(formula):
    i = 0
    while(i<len(formula)):
        print(formula[i])
        if (formula[i] in conec):
            if ((formula[i+1] in alfabeto) or (formula[i+1] in conec)):
                return True
            else:
                return False
        else:
            return False
        i += 1


a = "((p&q)>(~q&~p))"

if conectivos(a):
    print("jfkajshdfas")