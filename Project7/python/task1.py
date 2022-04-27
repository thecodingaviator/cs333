# Memory management in Python
# Parth and Chandra
# 4/25/2022



def main():
  # All statements that create memory
  a = [1, 2, 3]
  b = 5
  c = a

  # All statements that release memory
  a = None
  print("Before a is set to None")
  print("a:", a) # Should print nothing
  print("After a is set to None")

  b = None
  c = None

  print("b:", b)
  print("c:", c)

if __name__ == "__main__":
  main()