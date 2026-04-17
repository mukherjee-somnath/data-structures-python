def callingFunction(n):
  if(n>0):
    print(n, end=' ')
    callingFunction(n-1)

def returnFunction(n):
  if(n>0):
    returnFunction(n-1)
    print(n, end=' ')
  
def main():
  callingFunction(5)
  print()
  returnFunction(5)
  print()

main()
