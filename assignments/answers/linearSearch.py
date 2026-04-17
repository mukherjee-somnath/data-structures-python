# Python program to demonstrate working of linear search


def loadArray():
  data = [0]*10;
  for i in range(0,10):
    data[i] = pow(2,i)
  return data

def showArray(data):
  for i in range(len(data)):
    print(data[i], end=" ")
  print()

def main():
  data = loadArray()
  showArray(data)
  element = int(input("Enter the element to be searched: "))
  sentinelLinearSearch(data, element)

# Linear search
def linearSearch(data, element):
  for i in range(len(data)):
    if data[i] == element:
      print(element, "found at position", i+1)
      return
  print(element, "not found")

# Sentinel linear search
def sentinelLinearSearch(data, element):
  # Replace the last element with the element to be searched for
  n = len(data)
  lastElement = data[n-1]
  data[n-1] = element
  
  # Search for the element
  i=0
  while(data[i] != element):
    i+=1

  # Replace the last element back
  data[n-1] = lastElement

  # Print the result
  if(i<n-1) or lastElement == element:
    print(element, "found at position", i+1)
  else:
    print(element, "not found")

main()