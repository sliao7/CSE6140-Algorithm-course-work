def f(a1,a2,a3):
	ans = max(sum(a1), a1[0]+sum(a2), a1[0]+a2[0]+sum(a3))
	print('completing time:', ans)
	return ans


a1 = [3,9,6]
a2 = [1,4,11]
a3 = [5,7,8]

ans = []

print('a1, a2, a3')
ans.append(f(a1, a2, a3))

print('a1, a3, a2')
ans.append(f(a1, a3, a2))

print('a2, a,1 a3')
ans.append(f(a2, a1, a3))

print('a2, a3, a1')
ans.append(f(a2, a3, a1))

print('a3, a1, a2')
ans.append(f(a3, a1, a2))

print('a3, a2, a1')
ans.append(f(a3, a2, a1))

print('Minimum finishing time:', min(ans))