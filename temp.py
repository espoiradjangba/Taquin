import itertools

n = eval(input("Entrez la taille du taquin >"))
elements = [item for item in range(0, n**2)]
etats = list(itertools.permutations(elements))
# position de zero
etats_avec_zero = []
for i in range(n):
    for j in range(n):
        indice = n * i + j
        etats = list(itertools.permutations([item for item in range(1, n**2)]))
        for etat in etats:
            etat = list(etat)
            etat.insert(indice, 0)
            print(etat)
for i in range(n):
    for j in range(n):
        for element in list(itertools.permutations([k for k in range(1, n**2)])):
            l_element = list(element)
            s1 = l_element[: i * n + j] + [0] + l_element[i * n + j :]
            print(s1)
