# Parth Parth and Chandrachud Gowda
# 03/09/2022
# Demonstrate Control Flow statements

def main():
  # types of if statements
  a=1

  print("EG 1:")
  # Regular if
  if(a==1):
    print("a is 1")

  print("EG 2:")
  # if else
  if(a==1):
    print("a is 1")
  else:
    print("a is not 1")

  print("EG 3:")
  # if elif else
  if(a==1):
    print("a is 1")
  elif(a==2):
    print("a is 2")
  else:
    print("a is neither 1 nor 2")

  print("EG 4:")
  # nested if
  b=5
  if(a==1):
    if(b==5):
      print("a is 1 and b is 5")
    else:
      print("a is 1 but b is not 5")
  else:
    print("a is not 1")

  print("EG 5:")
  # chained elif
  if(a==1):
    if(b==5):
      print("a is 1 and b is 5")
    elif(b==6):
      print("a is 1 but b is 6")
    else:
      print("a is 1 but b is neither 5 nor 6")
  else:
    print("a is not 1")

  print("EG 6:")
  # for loops
  # the following code will print 1-10
  for i in range(0,10):
    print(i+1)

  print("EG 7:")
  # while loops
  # the following code will print 1-10
  i=0
  while(i<10):
    print(i+1)
    i=i+1

  print("EG 8:")
  # break and continue
  # break will break out of the current loop
  for i in range(0,10):
    if(i==5):
      break
    print(i)
  
  print("EG 9:")
  # continue will skip the rest of the loop and continue to the next iteration
  for i in range(0,10):
    if(i==5):
      continue
    print(i)

  print("EG 10:")
  # pass
  # pass is a placeholder for code that is not yet implemented
  # it can be used to prevent errors
  for i in range(0,10):
    if(i==5):
      pass
    print(i)

if __name__ == "__main__":
  main()
