# TP7: Resolution d'une equation par dichotomie

---

lien des tp: https://github.com/Bolk3/tp

---

## Fonction 1 : Existe

````python
def Existe(f, int):
    list_eval = []

    if int[0] > int[1]:
        for i in range(int[1], int[0]):
            temp = f.replace("x", str(i))
            list_eval.append(temp)
    else:
        for i in range(int[0], int[1]):
            temp = f.replace("x", str(i))
            list_eval.append(temp)

    for poss in list_eval:
        if eval(poss) == 0:
            return True
    return f"la fonction f(x) ne contient pas de racine dans l'intervale {int}"
````

cette fonction sert à evaluer le fait qu'une ou plusieurs racines de la fonction **f(x)** soient dans l'intervale donnée
les argument sont :

- f : la variable qui contient la fonction f(x),cette fonction est un string. le probleme principale de cette methode est la comprehention par le programe de la fonction.
- int: la variable qui contient la liste composée de deux element le debut de l'intervale ainsi que sa fin

la fonction retournera:

- True si une racine est trouvée
- f"la fonction f(x) ne contient pas de racine dans l'intervale {int}" si aucune racine est trouvée dans l'intervale

### fonctionement de la fonction

- <ins>etape 1</ins>: initialisation des variables
la fonction a deux variable **f** et **int** d'initialisée de base au lancement  de la fonction puis initialise la liste vide **list_eval**
- <ins>etape 2</ins>: generation des possibilités
les possibilitée sont generee grace a une boucle qui prend comme argument int[0] int[1] (et inversement si int[0] > int[1]) et le pas calculée grace a $$\frac{1}{10^{nbdecimale}}$$ <ins>*nbdecimale*</ins> etant le nombre de decimal maximum entre int[0] et int[1]
dans cette boucle on a une variable temporaire (**temp**) qui contient f dont les "x" sont remplacés par i le rang d'iteration de la boucle grace a la methode <ins>replace()</ins> puis est ajoutée dans la liste **list_eval**
- <ins>etape 3</ins>: evaluation des possibilités
les possibilitées sont evaluée grace à une boucle qui recupere chaques elements de la liste des posibilitées **list_eval** et qui, grace a la methode <ins>eval()</ins> effectue le calcul de chaques element. si un des elements est egal a 0 (C.à.d racine) la fonction revoie True, sinon si aucun n'est egal a 0 la fonction renvoie <ins>"la fonction f(x) ne contient pas de racine dans l'intervale {int}"</ins>

### exemple

nous prendrons comme exemple la fonction $f(x)=(x-1)^2$ sur l'intervale [-1, 5]

| nom                      | contenue                                   | code    |
|--------------------------|--------------------------------------------|---------|
| f                        | "(x-1)**2"                                 | etape 1 |
| int                      | [-1, 5]                                    | etape 1 |
| list_eval (au lancement) | []                                         | etape 1 |
| list_eval (apres code)   | ["(-1-1)**2", "(0-1)**2", ..., "(5-1)**2"] | etape 2 |

boucle "for ch in list_eval":

- eval(ch) ("(-1-1)**2") = 4
n'est pas egal a 0
- eval(ch) ("(0-1)**2") = 1
n'est pas egal a 0
- eval(ch) ("(1-1)**2") = 0
egal a 0 renvoie True
fin de boucle

## Fonction 2 : New_int
