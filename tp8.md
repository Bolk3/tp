<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="#5000ca" fill-opacity="1" d="M0,224L18.5,218.7C36.9,213,74,203,111,213.3C147.7,224,185,256,222,256C258.5,256,295,224,332,218.7C369.2,213,406,235,443,229.3C480,224,517,192,554,186.7C590.8,181,628,203,665,202.7C701.5,203,738,181,775,160C812.3,139,849,117,886,122.7C923.1,128,960,160,997,170.7C1033.8,181,1071,171,1108,186.7C1144.6,203,1182,245,1218,261.3C1255.4,277,1292,267,1329,234.7C1366.2,203,1403,149,1422,122.7L1440,96L1440,0L1421.5,0C1403.1,0,1366,0,1329,0C1292.3,0,1255,0,1218,0C1181.5,0,1145,0,1108,0C1070.8,0,1034,0,997,0C960,0,923,0,886,0C849.2,0,812,0,775,0C738.5,0,702,0,665,0C627.7,0,591,0,554,0C516.9,0,480,0,443,0C406.2,0,369,0,332,0C295.4,0,258,0,222,0C184.6,0,148,0,111,0C73.8,0,37,0,18,0L0,0Z"></path></svg>

# <p class="titre">Tp6: Fonctions et Graphiques</p>

---

lien des tp: https://github.com/Bolk3/tp

---

### 1.Problematique

### 2.Fonctionement grossier du code

# <p class="titre">Fonctionement en detail du code</p>

### f_moyenne

````python
def f_moyenne(l:list):
    r = 0
    for element in l:
        r += element
    return r/len(l)
````

### f_indice

````python
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
````

### f_terme

````python
def f_termes(i:int, L:list, n:int):
    poss = i-1
    r = []
    r.append(L[poss])
    for j in range(n):
        r.append(L[poss - j])
    for j in range(n):
        r.append(L[poss + j])
    return r
````

### f_lissage

````python
def f_lissage(L:list, n:int):
    r = []
    for i in range(len(L)):
        moyenne = []
        
        moyenne.append(L[i])
        for j in range(1, n+1):
            if i-j > 0:
                moyenne.append(L[i-j])
        for j in range(1, n+1):
            if i+j <= len(L)-1:
                moyenne.append(L[i+j])
                
        r.append(sum(moyenne)/len(moyenne))
    return r
````

### f_affiche_list

````python
def f_affiche_liste(fig_i:int, Liste_x:list, liste_Y:list):
    import matplotlib.pyplot as plt 
    x_lisse , y_lisse = f_lissage(Liste_x, 1), f_lissage(liste_Y, 1)
    plt.plot(Liste_x, liste_Y, "r")
    plt.plot(x_lisse, y_lisse, "b--")
    plt.title("Figure " + str(fig_i))
    plt.show()
````

### f_somme

````python
def f_somme(L:list):
    r = 0
    for element in L:
        r += element
    return r
````

### f_somme_prod

````python
def f_somme_prod(L1:list, L2:list):
    return f_somme(L1) +f_somme(L2)
````

### f_equation_droite

````python
def f_equation_droite(Liste_x:list, Liste_y:list):
    xm = f_moyenne(Liste_x)
    ym = f_moyenne(Liste_y)
    a_h = 0
    a_b = 0
    for i in range(len(Liste_x)):
        a_h += (Liste_x[i] - xm) * (Liste_y[i] - ym)
    for i in range(len(Liste_x)):
        a_b += (Liste_x[i] - xm) ** 2
    a = a_h / a_b
    b = ym - a*xm
    return [a, b]
````

### f_n_dernier

````python
def f_n_dernier(n:int, L:list):
    r = []
    r.append(L[len(L)-1])
    for i in range(1, n+1):
        r.append(L[len(L) - n+1])
    return r
````

### f_ab

````python
def f_ab(Liste_x:list, Liste_y:list, Nb_Val:int):
    x_derniere = f_n_dernier(Nb_Val, Liste_x)
    y_derniere = f_n_dernier(Nb_Val, Liste_y)
    return f_equation_droite(x_derniere, y_derniere)
````

### f_objectif

````python
def f_objectif(a:float, b:float, Objectif):
    import numpy as np
    if a == 0:
        return np.inf
    else:
        x = (a * Objectif) + b 
        return x 
````

<style>

.titre {
    text-align: center;
}

</style>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="#5000ca" fill-opacity="1" d="M0,224L18.5,218.7C36.9,213,74,203,111,213.3C147.7,224,185,256,222,256C258.5,256,295,224,332,218.7C369.2,213,406,235,443,229.3C480,224,517,192,554,186.7C590.8,181,628,203,665,202.7C701.5,203,738,181,775,160C812.3,139,849,117,886,122.7C923.1,128,960,160,997,170.7C1033.8,181,1071,171,1108,186.7C1144.6,203,1182,245,1218,261.3C1255.4,277,1292,267,1329,234.7C1366.2,203,1403,149,1422,122.7L1440,96L1440,320L1421.5,320C1403.1,320,1366,320,1329,320C1292.3,320,1255,320,1218,320C1181.5,320,1145,320,1108,320C1070.8,320,1034,320,997,320C960,320,923,320,886,320C849.2,320,812,320,775,320C738.5,320,702,320,665,320C627.7,320,591,320,554,320C516.9,320,480,320,443,320C406.2,320,369,320,332,320C295.4,320,258,320,222,320C184.6,320,148,320,111,320C73.8,320,37,320,18,320L0,320Z"></path></svg>