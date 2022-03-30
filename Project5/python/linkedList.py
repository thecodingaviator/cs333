class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def __str__(self):
    # if list is empty, return empty string
    if self.head is None:
      return '[]'
    else:
      # Put all items in a list
      items = []
      current = self.head
      # Loop through list and add items to list
      while current is not None:
        items.append(current.data)
        current = current.next
      # Convert list to string
      return str(items)

  def push(self, data):
    new_node = Node(data)
    # if list is empty, set head and tail to new node
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    # if list is not empty, set new node's next to head and head to new node
    else:
      new_node.next = self.head
      self.head = new_node
    self.size += 1
    return self.head

  def append(self, data):
    new_node = Node(data)
    # if list is empty, set head and tail to new node
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    # if list is not empty, set new node's next to head and head to new node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.size += 1
    return self.tail

  def pop(self):
    # if list is empty, return None
    if self.head is None:
      return None
    # if list has only one item, set head and tail to None
    elif self.head == self.tail:
      popped = self.head.data
      self.head = None
      self.tail = None
      self.size -= 1
      return popped
    # if list has more than one item, set head to next item and decrement size
    else:
      popped = self.head
      self.head = self.head.next
      self.size -= 1
      return popped

  def remove(self, data, comparator):
    if self.head is None:
      return None
    else:
      current = self.head
      previous = None
      while current is not None:
        if comparator(current.data, data):
          if previous is None:
            self.head = current.next
          else:
            previous.next = current.next
          self.size -= 1
          return current.data
        previous = current
        current = current.next
      return None

  def getSize(self):
    return self.size

  def clear(self):
    self.head = None
    self.tail = None
    self.size = 0
    return self.head is None and self.tail is None and self.size == 0
  
  def map(self, func):
    if self.head is None:
      return None
    else:
      current = self.head
      while current is not None:
        current.data = func(current.data)
        current = current.next
      return self.head

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

  def __str__(self):
    return str(self.data)

def main():
  # Create list
  ll = LinkedList()

  # Push 1 to 10
  for i in range(1, 11):
    ll.append(i)

  # Print list
  print("List:", ll)
  print("Size: ", ll.getSize())

  # Pop front
  print("Pop: ", ll.pop())
  print("List:", ll)
  print("Size: ", ll.getSize())

  # Remove 5
  print("Remove 5:", ll.remove(5, lambda a, b: a == b))
  print("List:", ll)
  print("Size: ", ll.getSize())

  # Map each item in list to itself squared
  print("Map each item in list to itself squared:")
  print("Map:", ll.map(lambda a: a ** 2))
  print("List:", ll)
  print("Size: ", ll.getSize())

  # Clear list
  print("Clear list")
  ll.clear()
  print("List:", ll)
  print("Size: ", ll.getSize())

  # Push a to z and then print list
  for i in range(ord('z'), ord('a') - 1, -1):
    ll.push(chr(i))
  print("List:", ll)
  print("Size: ", ll.getSize())

if __name__ == '__main__':
  main()