def gcd(a, b):
    '''
    this function to find the greatest common divisor
    '''
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def toiGian(a, b):
    '''
    this function to simplify fractions
    '''
    x = gcd(a, b)
    a //= x
    b //= x
    return a, b

def multi(n):
    '''
    this function to multiply fractions and return result
    '''
    ts = ms = 1
    while n > 0:
        a, b = map(int, input().split())
        ts *= a
        ms *= b
        n -= 1

    ts, ms = toiGian(ts, ms)
    return ts, ms

n = int(input())
res_ts, res_ms = multi(n)
print(res_ts, res_ms)
