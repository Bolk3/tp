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
    pas = 1
    if int[0] > int[1]:
        pass
    
    if int[0] > int[1]:
        for i in range(int[1], int[0], pas):
            temp = f.replace("x", str(i))
            list_eval.append(temp)
    else:
        for i in range(int[0], int[1], pas):
            temp = f.replace("x", str(i))
            list_eval.append(temp)
    
    #evaluation de toutes les possibilités
    for poss in list_eval:
        if eval(poss) == 0:
            return True
    return f"la fonction f(x) ne contient pas de racine dans l'intervale {int}"

def New_int(f:str, int:list):
    """

    Args:
        f (str): fonction dans laquelle on recherche une racine 
        int (list): l'intervalle dans lequel la racine est recherchée 
    """
    pass

def Dichotomie(f:str, int:list, crit_x):
    """[summary]

    Args:
        f (str): [description]
        int (list): [description]
        crit_x ([type]): [description]
    """
    pass

if __name__ == "__main__":
    print(Existe("(x-1)**2", [-1, 5]))