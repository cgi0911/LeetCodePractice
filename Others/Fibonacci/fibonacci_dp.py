import time

def fibRecursive(n):
    """
    :type n: int
    :return: Fibonacci(n)
    :rtype: int
    """
    if (n <= 1):
        return n
    else:
        return (fibRecursive(n - 1) + fibRecursive(n - 2))
    

def _fibMemorization(n, lookup):
    """
    :type n: int
    :return: Fibonacci(n)
    :rtype: int
    """
    if (lookup[n] == None):
        if (n <= 1):
            lookup[n] = n
        else:
            lookup[n] = _fibMemorization(n - 1, lookup) + _fibMemorization(n - 2, lookup)
        
    return lookup[n]
    
    
def fibMemorization(n):
    """ Top-down dynamic programming
    :type n: int
    :return: Fibonacci(n)
    :rtype: int
    """
    lookup = [None] * 10000
    return _fibMemorization(n, lookup)
    
    
    
def fibTabulation(n):
    """ Bottom-up dynamic programming
    :type n: int
    :return: Fibonacci(n)
    :rtype: int
    """
    lookup = [None] * 10000
    lookup[0] = 0
    lookup[1] = 1
    
    for i in range(2, n + 1):
        lookup[i] = lookup[i - 1] + lookup[i - 2]
    
    return lookup[n]


if __name__ == "__main__":
    n = int(input("Input n: "))
    
    st = time.time()
    res = fibMemorization(n)
    el = time.time() - st
    print ("Fibonacci(%d) by top-down memorization: %d" %(n, res))
    print ("Elapsed time = %f seconds" %(el))
    
    st = time.time()
    res = fibTabulation(n)
    el = time.time() - st
    print ("Fibonacci(%d) by bottom-up tabulation: %d" %(n, res))
    print ("Elapsed time = %f seconds" %(el))
    
    st = time.time()
    res = fibRecursive(n)
    el = time.time() - st
    print ("Fibonacci(%d) by recursion: %d" %(n, res))
    print ("Elapsed time = %f seconds" %(el))    