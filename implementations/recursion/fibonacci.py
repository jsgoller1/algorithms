cache = {"calls":0}

def fib(n, depth=0):
  cache['recursive calls'] += 1
  if n in cache:
    return cache[n]
  print(depth*2*" "+"{0}: Calculating fib {1}".format(depth, n))
  depth+=1
  if n == 2:
    return 1
  if n == 1:
    return 1
  cache[n] = fib(n-1, depth) + fib(n-2, depth)
  return cache[n]

print(fib(55))
print(cache['recursive calls'])
