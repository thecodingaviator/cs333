# Parth Parth and Chandrachud Gowda
# 03/09/2022
# Implement generic list sort

class Sort:
  # implement quick sort using comparator function
  def quickSort(self, arr, comparator):
    self.quickSortHelper(arr, 0, len(arr)-1, comparator)  # sort the array

  def quickSortHelper(self, arr, low, high, comparator):
    if low < high:
      # pi is partitioning index, arr[pi] is now at right place
      pi = self.partition(arr, low, high, comparator)

      # Separately sort elements before partition and after partition
      self.quickSortHelper(arr, low, pi-1, comparator)
      self.quickSortHelper(arr, pi+1, high, comparator)

  # To find the partitioning index, we choose the last element as pivot
  # and move all smaller elements to left of pivot and larger elements to right
  def partition(self, arr, low, high, comparator):
    i = low-1  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
      # If current element is smaller than the pivot
      if comparator(arr[j], pivot):
        # increment index of smaller element
        i = i+1
        arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
  
def comparator(a, b):
  if a < b:
    return True
  else:
    return False

def main():
  s = Sort()
  arr = [12, 11, 13, 5, 6, 7]
  s.quickSort(arr, comparator)
  print(arr)

if __name__ == "__main__":
  main()
