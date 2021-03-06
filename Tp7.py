from math import sqrt

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
    moyenne = (int[1] + int[0])/2
    g_int, d_int = [int[0], moyenne], [moyenne, int[1]]
    
    r = []
    if Existe(f, g_int) == True:
        if g_int[0] > moyenne:
            distance = g_int[0] - moyenne
        else:
            distance = moyenne - g_int[0]
        temp = [g_int, distance]
        r.append(temp)
    
    if Existe(f, d_int) == True:
        if d_int[1] > moyenne:
            distance = d_int[1] - moyenne
        else:
            distance = moyenne - d_int[1]
        temp = [d_int, distance]
        r.append(temp)
        
    return r
    
def Dichotomie(f:str, int:list, crit_x):
    """effectue la recherche de racine jusqu'a 10**-(crit_x)

    Args:
        f (str): fonction 
        int (list): [description]
        crit_x ([type]): [description]
    """
    i = 0
    nv_int = New_int(f, int)
    moyenne = (nv_int[0][0][0] + nv_int[0][0][1]) /2
    h = str(moyenne).split(".")[1]
    while len(h) < crit_x:
        nv_int = New_int(f, nv_int[0][0])
        moyenne = (nv_int[0][0][0] + nv_int[0][0][1]) /2
        h = str(moyenne).split(".")[1]
        i += 1
    return [moyenne, i]

def main():
    fonction = input("quelle est votre fonction (celle-ci doit etre monotone):\n")
    
    while True:
        try:
            min_int = float(input("quel est le minimum de l'intervalle de la fonction:\n"))
            break
        except:
            print("la valeur n'est pas possible")
    
    while True:
        try:
            max_int = float(input("quel est le maximum de l'intervalle de la fonction:\n"))
            break
        except:
            print("la valeur n'est pas possbile")
    
    while True:
        try:
            degres = int(input("quelle est la pressition de la methode dichotomique?:\n"))
            if degres > 0:
                break
        except:
            print("la valeur n'est pas possible")
    
    reponse = Dichotomie(fonction, [min_int, max_int], degres)
    print(f"avec la methode dichotomique la racine est de {reponse[0]} avec une pressition de 10**-{degres}\nla fonction s'est repetée {reponse[1]} fois")
        
if __name__ == "__main__":
    main()