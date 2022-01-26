import random

def zapiszPlik(nazwaPliku, dane, x, y):
    with open(nazwaPliku,'w') as plik:
        for i in range(y):
            for j in range(x):
                dane[i][j] = str(dane[i][j])
            plik.write(' '.join(dane[i]))
            plik.write("\n")
        plik.close()


def otworzPlik(nazwaPliku, x, y):
    with open(nazwaPliku,'r') as plik:
        content = plik.readlines()
        plik.close()

    for i in range(y):
        content[i] = content[i].split(" ")
        for j in range(x):
            content[i][j] = int(content[i][j])
    return content


if __name__ == "__main__":

    l_ciagow = 100

    # procesy

    l_procesow = 100

    t_przybycia = [[0 for x in range(l_procesow)] for y in range(l_ciagow)]
    t_wykonania = [[0 for x in range(l_procesow)] for y in range(l_ciagow)]

    random.seed(54821)
    for i in range(l_ciagow):
        for j in range(l_procesow):
            t_przybycia[i][j] = random.randint(1,50)                     
            t_wykonania[i][j] = random.randint(1,20)

    # zastępywanie stron

    l_stron = 100

    nr_stron = [[0 for x in range(l_stron)] for y in range(l_ciagow)]
    random.seed(54821)
    for i in range(l_ciagow):
        for j in range(l_stron):
            nr_stron[i][j] = random.randint(1,20)                   

    zapiszPlik("przybycie.txt", t_przybycia, l_procesow, l_ciagow)
    zapiszPlik("wykonanie.txt", t_wykonania, l_procesow, l_ciagow)
    zapiszPlik("strony.txt", nr_stron, l_stron, l_ciagow)
