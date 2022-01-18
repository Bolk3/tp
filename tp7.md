# <p style="text-align: center;">TP7: <ins>Resolution d'une equation par dichotomie</ins></p>

---

lien des tp: https://github.com/Bolk3/tp

---

## <p style="text-align: center;"> Fonctionement generale du projet</p>

### 1.Problematique
Le cahier des charges est tel que:
- le programme doit calculer la ou les deux racines de la fonction f(x)
- le programme doit donner les largeurs des l'intervalles des racines et donc leur impressision
- le programme doit donner son nombre d'iterations pour trouver
- le programme doit donner un comparatif entre le calcul par methode dichotomique et la vraie racine

### 2.Fonctionement grossier du code
le programme demande a l'utilisateur 3 elements:

- la fonction f(x)
- l'intervalle
- et la pressition recherchée de l'algorithme

puis initialise une instance de la fonction **Dichotomie** qui initie une boucle dans laquelle on obtient une liste de deux element grace a la fonction **New_int** si les deux element puis on verifie 
## <p style="text-align: center;"> Fonctionement en detail du projet</p>

### 1.Range_f

````python
def Range_f(debut, fin, pas=1):
    r, i = [debut], debut
    while i < fin:
        i += pas
        r.append(i)
    return r
````

cette fonction sert a contourné un probleme rencontrée durant la conception de la fonction **Existe**. le probleme etant que la mehode **Range** ne prend pas en compte les variables de type float. son fonctionement est simple, il consiste en une boucle while qui ajoute dans une liste une variable i qui est le debut + (n* le pas) tans que i n'est pas egal ou supperieur a la valeur de fin.

### 2.Existe

````python
def Existe(f:str, int:list):
    list_eval = []

    g,d = str(int[0]).split("."), str(int[1]).split(".")
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
    
    for poss in list_eval:
        if eval(poss) == 0:
            return True
    return f"la fonction f(x) ne contient pas de racine dans l'intervale {int}"
````
### 3.New_int

````python
def New_int(f:str, int:list):
    moyenne = int[0]+int[1]/2
    g_int, d_int = [int[0], moyenne], [moyenne, int[1]]

    if Existe(f, g_int) == True and Existe(f, d_int) == True:
        distance_g, distance_d = g_int[0] - g_int[1] if g_int[0] > g_int[1] else g_int[1] - g_int[0], d_int[0] - d_int[1] if d_int[0] > d_int[1] else d_int[1] - d_int[0]
        return[[distance_g, g_int],[distance_d, d_int]]
    elif Existe(f, g_int) == True:
        if g_int[0] > g_int[1]:
            distance = g_int[0] - g_int[1]
        else:
            distance = g_int[1] - g_int[0]
        return [g_int, distance]
    else:
        if d_int[0] > d_int[1]:
            distance = d_int[0] - d_int[1]
        else:
            distance = d_int[1] - d_int[0]
        return [d_int, distance]
````

### 4.Dichotomie

````python
````
