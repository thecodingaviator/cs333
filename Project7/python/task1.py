# Memory management in Python
# Parth and Chandra
# 4/25/2022

def main():
  # All statements that create memory
  a = [1, 2, 3]
  b = 5
  c = a

  print("a: ", a)
  # All statements that release memory
  del a
  # If I try to print a, it will throw an error
  #print(a)

  print("c: ", c)

  a = 40      # Create object <40>
  b = a       # Increase ref. count  of <40>
  c = [b]     # Increase ref. count  of <40>
  del a       # Decrease ref. count  of <40>
  b = 100     # Decrease ref. count  of <40>
  c[0] = -1   # Decrease ref. count  of <40>

if __name__ == "__main__":
  main()
