#Python
#Algorytm zastępywania stron FIFO

import random
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
    zawartosc_ramki = [0] * ramki[k]
    index = 0
    for i in range(l_ciagow):
            for j in range(l_stron):
                if nr_stron[i][j] not in zawartosc_ramki:
                    zawartosc_ramki[index] = nr_stron[i][j]
                    index = wyliczIndex(index, ramki[k])
                    ile[k] += 1
                
print("\nŚrednia liczba brakujących stron dla ramki o zakresie 3:", ile[0])
print("Średnia liczba brakujących stron dla ramki o zakresie 5:", ile[1])
print("Średnia liczba brakujących stron dla ramki o zakresie 7:", ile[2],end='\n\n')

################################  LRU ###################################

# for k in range(len(ramki)):
#     zawartosc_ramki = [0] * ramki[k]
#     index = 0
#     for i in range(l_ciagow):
#             for j in range(l_stron):
#                 if nr_stron[i][j] not in zawartosc_ramki:
#                     zawartosc_ramki[index] = nr_stron[i][j]
#                     index = wyliczIndex(index, ramki[k])
#                     ile[k] += 1
