import random

l_ciagow = 100
l_procesow = 100

t_przybycia = [[0 for x in range(l_procesow)] for y in range(l_ciagow)]
t_wykonania = [[0 for x in range(l_procesow)] for y in range(l_ciagow)]


random.seed(54821)
for i in range(l_ciagow):
    for j in range(l_procesow):
        t_przybycia[i][j] = random.randint(1,50)                       #arrival time            zwiększ jeśli będzie mała różnica z innym algorytmem
        t_wykonania[i][j] = random.randint(1,20)


# [10,20,30]
# ["10",20,30]
# ["10","20","30"]
# "10 20 30" - ' '.join()

with open("przybycie.txt",'w') as file_p:
    for i in range(l_ciagow):
        for j in range(l_procesow):
            t_przybycia[i][j] = str(t_przybycia[i][j])
        file_p.write(' '.join(t_przybycia[i]))
        file_p.write("\n")
    file_p.close()
    

with open("wykonanie.txt",'w') as file_w:
    for i in range(l_ciagow):
        for j in range(l_procesow):
            t_wykonania[i][j] = str(t_wykonania[i][j])
        file_w.write(' '.join(t_wykonania[i]))
        file_w.write("\n")
    file_w.close()


