# Parth Parth and Chandrachud Gowda
# 04/03/2022
# Python program to read a file, count the frequency of words and display the top 20 words

# Class to store the word and its frequency
class Word:
  def __init__(self, word, count):
    self.word = word
    self.count = count

  def __str__(self):
    return self.word + " " + str(self.count)

# Class to read the file and store words in a dictionary
class FileReader:
  def __init__(self, filename):
    self.filename = filename
    self.words = {}
    self.sortedWords = []

  # Read the file and store the words in a dictionary
  def read(self):
    with open(self.filename, 'r') as f:
      for line in f:
        for word in line.split():
          # Make the word lowercase and remove punctuation and whitespace
          word = word.lower()
          word = word.strip('.,:;?!')
          # If word is in the dictionary, increment its count
          if word in self.words:
            self.words[word] += 1
          # Else add the word to the dictionary with count 1
          else:
            self.words[word] = 1

  # Sort the words in the dictionary and return the top 20 words
  def sort(self):
    self.sortedWords = sorted(self.words.items(), key=lambda x: x[1], reverse=True)[:20]

# Main function
def main():
  filename = input("Enter the filename: ")
  fr = FileReader(filename)
  fr.read()
  fr.sort()
  for word in fr.sortedWords:
    print(word[0], ":", word[1])

if __name__ == "__main__":
  main()