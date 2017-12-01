def multiplication_table(m, n):
    print("")
    for j in range(1,10):
        for i in range(m,n+1):
            print("%d*%d=%2d" % (i,j,i*j),end="    ")
        print("")

def pyramid(n):
    for i in range(1,n+1):
        print(' '*(n-i) + '='*(2*i-1))
        
