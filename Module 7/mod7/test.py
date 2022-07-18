def first(x):
  x += 8
  print(1,x)
  def second(y):
    print(2,x,y)
    return x + y
  return second