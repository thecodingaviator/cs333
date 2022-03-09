# Parth Parth and Chandrachud Gowda
# 03/02/2022
# Demonstrate Functions as a data type

def do_a_thing(the_doer, the_thing):
  the_doer(the_thing)

def print_it(thing):
  print(thing)

def main():
  do_a_thing(print_it, "Using method directly: Hello World")
  a_variable = print_it
  a_variable("Using a_variable: Hello World")
  do_a_thing(a_variable, "Using do_a_thing with a_variable: Hello World")

square = lambda x: x * x

def main2():
  print(square(5))

if __name__ == "__main__":
  main()
  main2()
