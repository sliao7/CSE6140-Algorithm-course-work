### This is the code to use dynamical programming to solve problem 1 in HW2 for CSE 6140
D, W, M = 2, 7, 20
days = [0,1,1,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,1,1,1,1,0,0]
Memo = [0]*len(days)


def f(i):
    if Memo[i] == 0:
        if days[i] == 0 and i > 0:
            Memo[i] = f(i-1)
        else:
            if i <= 0:
                return 0
            else: 
                minfee = min(f(i-1) + D, f(i-7) + W, f(i-30) + M) 
                Memo[i] = minfee
    return Memo[i]
f(len(days)-1)
print(Memo)


Memo = [0]*len(days)            
def g(i):
    if i <= 0:
        return 0
    if Memo[i] == 0:
        if days[i] == 0:
            Memo[i] = g(i-1)
        else:
            Memo[i] = min(g(i-1) + D, g(i-7) + W, g(i-30) + M)
    return Memo[i]

g(len(days)-1)
print(Memo)



def print_message(i, d):
    print('Buy a $' + str(d) + ' dolloar ticket on day ', i)

def find_solution(i):
    if i<= 0:
        return
    
    if days[i] == 1:
        if Memo[i] == Memo[max(0, i-1)] + D:
            print_message(max(1, i), D)
            find_solution(i-1)
        if Memo[i] == Memo[max(0, i-7)] + W:
            print_message(max(1, i-6), W)
            find_solution(i-7)
        if Memo[i] == Memo[max(0, i - 30)] + M:
            print_message(max(1, i - 29), M)
            find_solution(i - 30)
    else:
        find_solution(i-1)

day = 29
print('The minimum fee George needs to pay for the first ', day, 'days are', Memo[day])
find_solution(day)
