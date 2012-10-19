def fib_iter(n):
    '''generate Fibonacci Numbers'''
    a, b = 0, 1
    while n:
        yield a
        a, b = b, a + b
        n -= 1

#print [each for each in fib_iter(10)]


def prime_iter(n):
    '''generate Prime Numbers'''
    table = [True for i in xrange(n+1)]
    for i in xrange(2, n+1):
        if table[i]:
            yield i
            for i in xrange(i*i, n+1, i):
                table[i] = False

#print [each for each in prime_iter(1000)]


def fac_iter(n):
    '''generate factors of n'''
    for i in xrange(2, n+1):
        while n % i == 0:
            yield i
            n /= i
        if n < i: break

#p3
#print [each for each in fac_iter(600851475143)]

def gen_partion(n, gen_with):
    '''count of generating n with numbers in gen_with, no 0 and no same numbers in get_with'''
    ans = [0 if i else 1 for i in xrange(n+1)]
    for each in gen_with:
        for i in xrange(each, n+1):
            ans[i] += ans[i - each]
    return ans


#print gen_partion(100, xrange(1, 100))[100]
