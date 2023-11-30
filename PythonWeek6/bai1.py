def MyMultiple (*args):
    '''
    multiply parameters
    parameters: *args (tuple) (*args: tham số biến động)
    return: int or float: result 

    '''
    multi = 1.0
    for i in args:
        multi *= i
    return multi

print(MyMultiple(1,2,3,4))
print(MyMultiple(5,5,5))
print(MyMultiple(1.2,5))

