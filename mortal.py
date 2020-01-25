def fib_mortal(n,m):
    fibo = [1,1]
    for i in range(2,n+1,1):
        if i < m: f = fibo[i-1] + fibo[i-2]
        elif i == m: f= fibo[i-1] + fibo[i-2] - 1
        else: f = fibo[i-1] + fibo[i-2] - fibo[i-(m+1)]
        fibo.append(f)
    return fibo[n]
