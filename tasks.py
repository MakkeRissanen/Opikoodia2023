def main():
  sum(40,30)
  iter()
  evenIndex("pynative")
  removechars("pynative",2)
  checkFirstAndLast([10,20,30,40,20])


def sum(value1, value2):
  if value1 * value2 < 1000:
    print(value1 * value2)
  else:
    print(value1 + value2)

def iter():
  number = 0
  previousnumber = 0
  for i in range(10):
    print("Current Number",number,"Previous Number",previousnumber,"Sum:",(number + previousnumber))
    previousnumber = number
    number = number + 1

def evenIndex(word):
  size = len(word)
  for i in range(0, size -1, 2):
    print(word[i])

def removechars(word, amount):
  word = word[amount:]
  print(word)

def checkFirstAndLast(array):
  firstChar = array[0]
  lastChar = array[len(array)-1]
  if firstChar == lastChar:
    print("true")
  else:
    print("false")
testi




if __name__ == "__main__":
  main()