# Problem 1: MARTA tickets
Memo = [0]*365            
def OPT(i):
    if i <= 0:
        return 0
    if Memo[i] == 0:
        if i not in days:
            Memo[i] = OPT(i-1)
        else:
            Memo[i] = min(OPT(i-1) + ticket[0], OPT(i-7) + ticket[1], OPT(i-30) + ticket[2])
    return Memo[i]


# Problem 2: Buying Computers
ndays = len(d) - 1



def opt(i,k):
    # base case
    if i == 1:
        return R

    # two options available
    if d[i] + k <= I:
        return min(opt(i-1, d[i] + k) + (d[i] + k)*C, opt(i-1, 0) + R)
    else:
        # has to order
        return opt(i-1,0) + R

Memo = [[0 for _ in range(I+1)] for _ in range(len(d))]
# base case
for k in range(I+1):
    Memo[1][k] = R

# bottom up
for i in range(2, len(d)):
    for k in range(I+1):
        if d[i] + k <= I:
        # two options available
            Memo[i][k] = min(Memo[i - 1][d[i] + k] + (d[i] + k) * C, Memo[i - 1][0] + R)
        else:
        # has to order
            Memo[i][k] = Memo[i - 1][0] + R

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