def is_prime(n):
    if n <= 1:
      return False  
    for i in range(2, n):
      if n % i == 0:
          return False
    return True

result = []

for i in range(100, 0, -1):
    if is_prime(i):
        continue
    if i % 15 == 0:
        result.append("FooBar")
    elif i % 3 == 0:
        result.append("Foo")
    elif i % 5 == 0:
        result.append("Bar")
    else:
        result.append(str(i))

print(" ".join(result))
