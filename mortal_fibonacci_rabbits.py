import collections

def tree():
    return collections.defaultdict(tree)

def matrix(x, m):
    mat = tree()
    for k in range (1,m+1):
        #first dimension: number of months the rabbits are alive (m)
        # second dimension: the order f the month that we examine each time 
        mat[k][1]=0
    #first month ==> entry only in mat[1]
    # we start with one rabbit
    mat[1][1] = 1
    mat[1][2] = 0
    for index in range(2,x):
        sum_mat = 0
        for k in range (2, m+1):
            mat[k][index] = mat[k-1][index-1]
            sum_mat += mat[k][index]
        # set the newborns of the next month
        mat[1][index+1] = sum_mat     

    total = 0

    for t in range(1,m+1):
        total+=mat[t][x-1]
    return total

if __name__ == '__main__':
    months = 81
    print matrix(months+1, 20)