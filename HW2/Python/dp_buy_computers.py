d = [None,2,4,5,3,1,3,1,7,9]
I = 15
R = 15
C = 1
ndays = len(d) - 1

Memo = [[0 for _ in range(I+1)] for _ in range(len(d))]

def opt(i,k):

    if i == 1:
        return R
    if d[i] + k <= I:
        return min(opt(i-1, d[i] + k) + (d[i] + k)*C, opt(i-1, 0) + R)
    else:
        return opt(i-1,0) + R

# for i in range(1,8): 
#     print('The first ', i, ' days needs ', opt(i,0), ' dollar.')

for k in range(I+1):
    Memo[1][k] = R

for i in range(2, len(d)):
    for k in range(I+1):
        if d[i] + k <= I:
            Memo[i][k] = min(Memo[i - 1][d[i] + k] + (d[i] + k) * C, Memo[i - 1][0] + R)
        else:
            Memo[i][k] = Memo[i - 1][0] + R

# print(Memo)

ans = Memo[-1][0]

def print_solution(i,n):
    print("Chuck should order ", n, " computers in the ", i, "th month." )


def find_solution(i,k):
    if i == 1:
        print_solution(i, d[i] + k)
        return 
    if Memo[i][k] == Memo[i - 1][0] + R:
        print_solution(i, d[i] + k)
        find_solution(i-1,0)
    else:
        print_solution(i, 0)
        find_solution(i-1, d[i] + k)

find_solution(ndays,0)

