#Python
#Algorytmy zastępywania stron FIFO(bez modyfikacji) i LRU

import obsluga_plikow

def wyliczIndex(index, zakres):
    if index < zakres-1:
        index += 1
    else:
        index = 0
    return index


l_ciagow = 100
l_stron = 100

nr_stron = obsluga_plikow.otworzPlik("strony.txt", l_stron, l_ciagow)

ramki = [3, 5, 7]
ile = [0, 0, 0]


for k in range(len(ramki)):
    for i in range(l_ciagow):
        zawartosc_ramki = [0] * ramki[k]
        index = 0
        for j in range(l_stron):
            if nr_stron[i][j] not in zawartosc_ramki:
                zawartosc_ramki[index] = nr_stron[i][j]
                index = wyliczIndex(index, ramki[k])
                ile[k] += 1
 
print("\nŚrednia liczba brakujących stron dla ramki o zakresie 3:", ile[0])
print("Średnia liczba brakujących stron dla ramki o zakresie 5:", ile[1])
print("Średnia liczba brakujących stron dla ramki o zakresie 7:", ile[2],end='\n\n')


################################  LRU ###################################

ile2 = [0] * 3 

for k in range(len(ramki)):
    for i in range(l_ciagow):
        zawartosc_ramki = [0] * ramki[k]
        id = [0] * ramki[k]
        index = 0
        for j in range(l_stron):
            if nr_stron[i][j] not in zawartosc_ramki:
                zawartosc_ramki[id.index(min(id))] = nr_stron[i][j]
                index += 1
                id[id.index(min(id))] = index
                ile2[k] += 1
            else:
                index += 1
                id[zawartosc_ramki.index(nr_stron[i][j])] = index

print("\nŚrednia liczba brakujących stron dla ramki o zakresie 3:", ile2[0])
print("Średnia liczba brakujących stron dla ramki o zakresie 5:", ile2[1])
print("Średnia liczba brakujących stron dla ramki o zakresie 7:", ile2[2],end='\n\n')


try:
    with open("wyniki_stron.txt", "x") as plik:
        plik.write("FIFO\n")
        for i in range(len(ile)):
            plik.write("Średnia liczba brakujących stron dla ramki o zakresie {}: {}\n".format(ramki[i],ile[i]))
        plik.write("LRU\n")
        for i in range(len(ile2)):
            plik.write("Średnia liczba brakujących stron dla ramki o zakresie {}: {}\n".format(ramki[i],ile2[i]))
        plik.close()

except FileExistsError:
    print("Plik o nazwie 'wyniki_stron.txt' już istnieje!")
    test = input("Czy chcesz go nadpisać? [Y/N]:")
    
    if test.lower() == 'y':
        with open("wyniki_stron.txt", "w") as plik:
            plik.write("FIFO\n")
            for i in range(len(ile)):
                plik.write("Średnia liczba brakujących stron dla ramki o zakresie {}: {}\n".format(ramki[i],ile[i]))
            plik.write("LRU\n")
            for i in range(len(ile2)):
                plik.write("Średnia liczba brakujących stron dla ramki o zakresie {}: {}\n".format(ramki[i],ile2[i]))
            plik.close()