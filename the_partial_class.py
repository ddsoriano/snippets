def add(x, y):
  return x + y
  
p_add = partial(add, 2)
p_add(4)                  # results in 6
