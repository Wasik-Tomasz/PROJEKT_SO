#Python
#testowanie algorytmu FCFS

import random 

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

#określanie czasów
random.seed(54821)
for i in range(l_ciagow):
    for j in range(l_procesow):
        t_przybycia[i][j] = random.randint(1,50)                       #arrival time            zwiększ jeśli będzie mała różnica z innym algorytmem
        t_wykonania[i][j] = random.randint(1,20)                       #burst time
                                          
        
# FCFS
t_przybycia_fcfs = t_przybycia

for i in range(l_ciagow):
    t_przybycia_fcfs[i].sort()                                               #sortowanie od najmniejszego czasu przybycia
    for j in range(l_procesow):                                        

        t_przetwarzania[i][j] = t_wykonania[i][j] + t_przybycia_fcfs[i][j]   #Turn around time 
        #t_czekania[i][j] = t_przetwarzania[i][j] - t_wykonania[i][j]    #waiting time

    t_czekania[i] = sprawdz_t_czekania(l_ciagow, t_wykonania[i], t_czekania[i], t_przybycia_fcfs[i])

    for j in range(l_procesow):
        t_realizacji[i][j] = t_przetwarzania[i][j] + t_czekania[i][j]   #Completion Time

    t_suma_czekania +=  sum(t_czekania[i])
    t_suma_przetwarzania += sum(t_przetwarzania[i])
    

t_srednia_czekania = t_suma_czekania/(l_procesow*l_ciagow)
t_srednia_przetwarzania= t_suma_przetwarzania/(l_procesow*l_ciagow)
 
print(t_srednia_czekania)
print(t_srednia_przetwarzania)



# with open("1.txt","w") as file:
#     file.writelines(str(t_przybycia_fcfs[0]))

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