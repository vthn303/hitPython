def input_array(n):
    '''
        input n numbers into an array
    params: n(int)
    return:array(list)
    '''
    array = list(map(int, input().split()))
    return array

def sum(array, x):
    '''
        return the sum of the elements of the array that are less than x
    params: array(list), x(int)
    return: sum(int)
    '''
    sum = 0
    for i in range(x+1):
        sum += array[i]
    return sum

n = int(input())
arr = input_array(n)
res = []
t = int(input())
while t > 0:
    x = int(input())
    res.append(sum(arr, x))
    t -= 1

#unpacking res 
print(*res, sep='\n')







