# Python program to demonstrate working of array

data = []

def space():
  print("\n"+"="*50)

# Inserting elements into the array by inserting at the beginning
def insert_first():
  space()
  value = input("Enter the element to be inserted at the beginning: ")
  data.insert(0, value)
  print(value, "inserted at the beginning.")
  display()

# Inserting elements into the array by appending at the end
def insert_last():
  space()
  value = input("Enter the element to be inserted at the end: ")
  data.append(value)
  print(value, "inserted at the end.")
  display()

# Inserting elements into the array by inserting at any position
def insert_index():
  space()
  index = int(input("Enter the index/position where the element has to be inserted: "))
  value = input("Enter the element to be inserted into the array: ")
  # data.insert(index, value)
  if index>len(data):
    data.append(value)
  elif index<0:
    data.insert(0, value)
  else:
    data.append(0)
    for i in range(len(data)-1, index-1, -1):
      data[i] = data[i-1]
    data[index-1] = value
    print(value, "inserted at the position", index)
  display()

def remove_first():
  data.pop(0)
  display()

def remove_last():
  data.pop()
  display()

# Removing elements from the array by index
def remove_index():
  index = int(input("Enter the index/position of the element to be removed: "))
  data.pop(index)
  display()
  # for i in range(index, len(data)):
  #     data[i] = data[i+1]
  # data.pop()

def search(element):
  for i in range(len(data)):
    if data[i] == element:
      print(element, "found at position", i+1)
      return
  print(element, "not found")



# Displaying the array
def display():
  print("The array is: ", end="")
  for i in range(len(data)):
    print(data[i], end=" ")

def main():
  
  while True:
    space()
    print("Enter the option you want to perform: ")
    switch = int(input("1. Insert at the start\t2. Insert at the end\t3. Insert at any position\n4. Remove from the start\t5. Remove from the end\t6. Remove from any position\n7. Search any element\n8. Display the array\n9. Exit\nEnter your choice: "))

    if switch == 1:
      insert_first()
    elif switch == 2:
      insert_last()
    elif switch == 3:
      insert_index()
    elif switch == 4:
      remove_first()
    elif switch == 5:
      remove_last()
    elif switch == 6:
      remove_index()
    elif switch == 7:
      search(input("Enter the element to be searched: "))
    elif switch == 8:
      display()
    elif switch == 9:
      print("Exiting...")
      break
    else:
      print("Invalid option!")
    print("\n")

main()
