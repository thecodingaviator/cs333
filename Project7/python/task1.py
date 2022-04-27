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

  a = 40      # Create object <40>
  b = a       # Increase ref. count  of <40>
  c = [b]     # Increase ref. count  of <40>
  del a       # Decrease ref. count  of <40>
  b = 100     # Decrease ref. count  of <40>
  c[0] = -1   # Decrease ref. count  of <40>

if __name__ == "__main__":
  main()