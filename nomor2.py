def triangular(x):
    if x == 1:
      return 1
    result = [i for i in range(x, 0, -1)]
    return sum(result)

print("Triangular is ", triangular(5))