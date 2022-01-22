#Python
#testowanie algorytmu FCFS z SJF

import obsluga_plikow

def sprawdz_t_czekania(l_ciagow, t_wykonania, t_czekania, t_przybycia):
    t_obslugi = [0] * l_ciagow
    t_obslugi[0] = 0
    t_czekania[0] = 0

    for i in range(1, l_ciagow):
        t_obslugi[i] = (t_obslugi[i - 1] + t_wykonania[i - 1])

        t_czekania[i] = t_obslugi[i] - t_przybycia[i]

        if(t_czekania[i] < 0):
            t_czekania[i] = 0

    return t_czekania


l_ciagow = 100
l_procesow = 100

# tworzenie tablic 100x100
t_przybycia = [[0 for x in range(l_procesow)] for y in range(l_ciagow)]
t_wykonania = [[0 for x in range(l_procesow)] for y in range(l_ciagow)]
t_realizacji = [[0 for x in range(l_procesow)] for y in range(l_ciagow)]
t_czekania = [[0 for x in range(l_procesow)] for y in range(l_ciagow)] 
t_przetwarzania = [[0 for x in range(l_procesow)] for y in range(l_ciagow)] 
t_suma_czekania = 0
t_suma_przetwarzania = 0

t_przybycia = obsluga_plikow.otworzPlik("przybycie.txt",l_procesow, l_ciagow)
t_wykonania = obsluga_plikow.otworzPlik("wykonanie.txt", l_procesow, l_ciagow)

# FCFS
t_przybycia_fcfs = t_przybycia

for i in range(l_ciagow):
   # t_przybycia_fcfs[i].sort()                    #sortowanie od najmniejszego czasu przybycia
    t_przybycia_fcfs, t_wykonania = zip(*sorted(zip(t_przybycia_fcfs, t_wykonania)))     
    t_przybycia_fcfs, t_wykonania = (list(t) for t in zip(*sorted(zip(t_przybycia_fcfs, t_wykonania))))
    for j in range(l_procesow):                                        

        t_przetwarzania[i][j] = t_wykonania[i][j] + t_przybycia_fcfs[i][j]   #Turn around time 

    t_czekania[i] = sprawdz_t_czekania(l_ciagow, t_wykonania[i], t_czekania[i], t_przybycia_fcfs[i])

    for j in range(l_procesow):
        t_realizacji[i][j] = t_przetwarzania[i][j] + t_czekania[i][j]   #Completion Time

    t_suma_czekania +=  sum(t_czekania[i])
    t_suma_przetwarzania += sum(t_przetwarzania[i])
    

t_srednia_czekania = t_suma_czekania/(l_procesow*l_ciagow)
t_srednia_przetwarzania= t_suma_przetwarzania/(l_procesow*l_ciagow)
 
print(t_srednia_czekania)
print(t_srednia_przetwarzania)


###############################################################################
#####################                  SJF                 ####################
###############################################################################

t_wykonania_sjf = t_wykonania
t_suma_czekania_sjf = 0
t_suma_przetwarzania_sjf = 0

for i in range(l_ciagow):
    t_wykonania_sjf[i].sort()         
    for j in range(l_procesow): 

        t_przetwarzania[i][j] = t_wykonania_sjf[i][j] + t_przybycia[i][j]   #Turn around time 

    t_czekania[i] = sprawdz_t_czekania(l_ciagow, t_wykonania_sjf[i], t_czekania[i], t_przybycia[i]) 

    for j in range(l_procesow):
        t_realizacji[i][j] = t_przetwarzania[i][j] + t_czekania[i][j]   #Completion Time

    t_suma_czekania_sjf +=  sum(t_czekania[i])
    t_suma_przetwarzania_sjf += sum(t_przetwarzania[i])

t_srednia_czekania_sjf = t_suma_czekania_sjf/(l_procesow*l_ciagow)
t_srednia_przetwarzania_sjf = t_suma_przetwarzania_sjf/(l_procesow*l_ciagow)


print(t_srednia_czekania_sjf) 
print(t_srednia_przetwarzania_sjf)

# plik = open("lokalizacja", "r")
# plik.writelines()
# plik.close()                                                                                                                                                                                          ###########################################################

# 'w' otwiera plik, jeżeli istnieje to usuwa jego zawartość
# 'a' dopisuje do końca pliku
# 'r+' otwiera w trybie r/w
# 'r' otwiera w trybie odczytu

try:
    with open("wyniki.txt", "x") as plik:
        plik.write("Średnia czekania FCFS: ")
        plik.write(str(t_srednia_czekania))
        plik.write("\nŚrednia przetwarzania FCFS: ")
        plik.write(str(t_srednia_przetwarzania))
        plik.write("\nŚrednia czekania SJF: ")
        plik.write(str(t_srednia_czekania_sjf))
        plik.write("\nŚrednia przetwarzania SJF: ")
        plik.write(str(t_srednia_przetwarzania_sjf))

        plik.close()
except FileExistsError:
    print("Plik o nazwie 'wyniki.txt' już istnieje!")
    test = input("Czy chcesz go nadpisać? [Y/N]:")
    
    if test.lower() == 'y':
        with open("wyniki.txt", "w") as plik:
            plik.write("Średnia czekania FCFS: ")
            plik.write(str(t_srednia_czekania))
            plik.write("\nŚrednia przetwarzania FCFS: ")
            plik.write(str(t_srednia_przetwarzania))
            plik.write("\nŚrednia czekania SJF: ")
            plik.write(str(t_srednia_czekania_sjf))
            plik.write("\nŚrednia przetwarzania SJF: ")
            plik.write(str(t_srednia_przetwarzania_sjf))
            plik.close()
