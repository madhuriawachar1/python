def recurSum(n):
    if n <= 1:
        return n
    return n + recurSum(n - 1)
  
# Driver code
n = 5
print(recurSum(n))


for i in range(4,2,-1):
    print(i)