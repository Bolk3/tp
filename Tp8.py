def f_moyenne(l:list):
    r = 0
    for element in l:
        r += element
    return r/len(l)


def f_indice(i:int, n:int, Nb_Termes:int):
    r = []
    liste_thermes = [j for j in range(Nb_Termes)]
    poss = liste_thermes.index(i)
    
    for j in range(n):
        try:
            r.append(liste_thermes[poss-j])
        except:
            continue
    for j in range(n):
        try:
            r.append(liste_thermes[poss+j])
        except:
            continue
    return r

def f_termes(i:int, L:list, n:int):
    poss = i-1
    r = []
    r.append(L[poss])
    for j in range(n):
        r.append(L[poss - j])
    for j in range(n):
        r.append(L[poss + j])
    return r


def f_lissage(L:list, n:int):
    r = []
    for i in range(len(L)):
        moyenne = []
        
        #obtenir les n element nessesaire au lissage
        moyenne.append(L[i])
        for j in range(n):
            try:
                moyenne.append(L[i-j])
            except:
                continue
        for j in range(n):
            try:
                moyenne.append(L[i+j])
            except:
                continue
        
        # prosses du lissage
        r.append(sum(moyenne)/len(moyenne))
    return r


def f_affiche_liste(fig_i:int, Liste_x:list, liste_Y:list):
    import matplotlib.pyplot as plt 
    plt.plot(Liste_x, liste_Y)
    plt.title("Figure " + str(fig_i))
    plt.show()


def f_somme(L:list):
    r = 0
    for element in L:
        r += element
    return r


def f_somme_prod(L1:list, L2:list):
    return f_somme(L1) +f_somme(L2)


def f_equation_droite(Liste_x:list, Liste_y:list):
    pass


def f_n_dernier(n:int, L:list):
    r = []
    r.append(L[len(L)-1])
    for i in range(1, n+1):
        r.append(L[len(L) - n+1])
    return r

def f_ab(Liste_x:list, Liste_y:list, Nb_Val:int):
    pass


def f_objectif(a:float, b:float, Objectif):
    import numpy as np
    if a == 0:
        return np.inf
    else:
        x = (a * Objectif) + b 
        return x 
    
if __name__ == "__main__":
    print(f_objectif(-1,10,5))