def Existe(f:str, int:list):
    """verifie si dans un intervale donnée la fonction f a au moins une racine

    Args:
        f (str): fonction dans laquelle on recherche une racine 
        int (list): l'intervalle dans lequel la racine est recherchée 
    
    Returns:
        r (bool): True si une racine est trouvée dans la fonction
    """
    list_eval = [eval(f.replace("x", str(int[0])))
                 , eval(f.replace("x", str(int[1])))]
    if list_eval[0] <= 0 and list_eval[1] >= 0:
        return True
    elif list_eval[0] >= 0 and list_eval[1] <= 0:
        return True
    else:
        return False

def New_int(f:str, int:list):
    """

    Args:
        f (str): fonction dans laquelle on recherche une racine 
        int (list): l'intervalle dans lequel la racine est recherchée 
    """
    moyenne = (int[0]+int[1])/2
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