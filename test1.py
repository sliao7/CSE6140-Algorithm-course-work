a = [1,4,2,8,6,5,3,9,7]
n = len(a)
count = 0
for j in range(n):
    for i in range(j+1,n):
        if a[i] < a[j]:
            count += 1
print(count)

def merge(s1,count1,s2,count2):
    n = len(s1)
    count = 0
    merged_list = []
    i = 1;j = 1
    while s1 and s2:
        if s1[i] > s2[j]:
            merged_list.append(s2[j])
            j += 1
            count += (n - i) # number of elements in s1 that is greater than s2[j]
        else:
            merged_list.append(s1[i])
            i += 1
    for number in s1[i:]:
        merged_list.append(number)
    for number in s2[j:]:
        merged_list.append(number)
    return merged_list, count + count1 + count2

def mergeSort(s):

    if len(s) == 1:
        return s, 0
    #Divide s into two halfs, s1 and s2
    s1, count1 = mergeSort(s1)
    s2, count2 = mergeSort(s2)

    L, count = merge(s1,count1,s2,count2)
    return L, count





