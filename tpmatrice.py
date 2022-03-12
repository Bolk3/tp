import numpy as np

K = np.array([[ 0., 1., 2.],
              [ 1., 1., 1.],
              [ 1., 5., 1.]])

B = np.array([[1000.],
              [2000.],
              [3000.]])

def Permute(M:object,i:int,j:int):
    """
    la fonction permute utilise des variable tempon pour remplacer deux ligne d'un array de numpy
    par exemple
    
    [O,1,2]      i,j = 0,1      [1,1,1]
    [1,1,1]     ==========>     [0,1,2]
    [1,5,1]                     [1,5,1]
    
    Args:
        M (object): matrice cree par array numpy
        i (int): premiere ligne permutée
        j (int): seconde ligne permutée 

    Returns:
        object: matrice copiée et dont les ligne i et j sont permutée
    """
    copied_array = np.copy(M)
    temp = np.copy(copied_array[i])
    copied_array[i] = copied_array[j]
    copied_array[j] = temp
    return copied_array


def Pivot_partiel(M:object, i:int):
    r = np.copy(M[i][0])
    for element in M[i]:
        if element >= r:
            r = np.copy(element)
    return r


def Transvection(M:object, i:int, j:int, mu:float):
    pass


def Annulation(K:object, B:object , i:int):
    pass


def Trigonalise(K:object, B:object):
    pass


def Resolution(K:object , B:object):
    pass