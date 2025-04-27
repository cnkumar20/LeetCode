from random import randint
def mat_2d(m,n):
    arr_2d = [[0 for y in range(m)] for x in range(n)]
    for r in range(m):
        i = randint(0,m)
        arr_2d[r][r] = i 
    print(arr_2d)


mat_2d(3,3)
