def Range_f(debut, arrive, pas=1):
    """fonction range valable avec les float 

    Args:
        debut (int ou float): debut de l'intervale
        arrive (int ou float): fin de l'intervale
        pas (int, optional): pas entre les valeur. par defaut à 1.

    Returns:
        r (list): resultat
    """
    r = [debut]
    i = debut
    while i < arrive:
        i += pas
        if len(str(pas)) != i:
            pass
        r.append(i)
    return r


def Existe(f:str, int:list):
    """verifie si dans un intervale donnée la fonction f a au moins une racine

    Args:
        f (str): fonction dans laquelle on recherche une racine 
        int (list): l'intervalle dans lequel la racine est recherchée 
    
    Returns:
        r (bool): True si une racine est trouvée dans la fonction
    """
    list_eval = []
    #creation de toute les possibles variation de f
    #determination du pas nessesaire
    g,d = str(int[0]).split("."), str(int[1]).split(".")
    if len(g) == 1 and len(d) == 1:
        pas = 1
    else:
        if len(g) > len(d):
            pas = 1/10**len(g[1])
        elif len(g) < len(d):
            pas = 1/10**len(d[1])
        else:
            if len(g[len(g)-1]) > len(d[len(d)-1]):
                pas = 1/10**len(g[len(g)-1])
            else:
                pas = 1/10**len(d[len(d)-1])
    
    if int[0] > int[1]:
        for i in Range_f(int[1], int[0], pas):
            temp = f.replace("x", str(i))
            list_eval.append(temp)
    else:
        for i in Range_f(int[0], int[1],pas):
            temp = f.replace("x", str(i))
            list_eval.append(temp)
    
    #evaluation de toutes les possibilités
    negpos = False
    if eval(list_eval[0]) < 0:
        for poss in list_eval:
            if eval(poss) >= 0:
                negpos = True
    else:
        for poss in list_eval:
            if eval(poss) <= 0:
                negpos = True
    
    if negpos == True:
        return True
    return f"la fonction f(x) ne contient pas de racine dans l'intervale {int}"

def New_int(f:str, int:list):
    """

    Args:
        f (str): fonction dans laquelle on recherche une racine 
        int (list): l'intervalle dans lequel la racine est recherchée 
    """
    moyenne = int[0]+int[1]/2
    g_int, d_int = [int[0], moyenne], [moyenne, int[1]]
    if g_int[0] > g_int[1]:
        d_gauche = g_int[0] - g_int[1]
    else:
        d_gauche = g_int[1] - g_int[0]

    if d_int[0] > d_int[1]:
        d_droite = d_int[0] - d_int[0]
    else:
        d_droite = d_int[1] - d_int[0]
        
    if Existe(f, g_int) == True and Existe(f, d_int) == True:
        return [[g_int, d_gauche], [d_int, d_droite]]
    else:
        if Existe(f, g_int) == True:
            return [g_int, d_gauche]
        else:
            return [d_int, d_droite]
    
    
def Dichotomie(f:str, int:list, crit_x):
    """effectue la recherche de racine jusqu'a 10**-(crit_x)

    Args:
        f (str): fonction 
        int (list): [description]
        crit_x ([type]): [description]
    """
    i = 0
    nv_int = New_int(f, int)
    for i in range(4):
        nv_int = New_int(f, nv_int[0])
    return nv_int
        
print(Dichotomie("(x+1)**2", [-1, 5], 4))