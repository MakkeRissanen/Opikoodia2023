def main():
  list1 = [10, 20, 25, 30, 35]
  list2 = [40, 45, 60, 75, 90]
  sum(40,30)
  iter()
  evenIndex("pynative")
  removechars("pynative",2)
  checkFirstAndLast([10,20,30,40,20])
  divisible5([5,14,22,25,30])
  countwords("Emma","Emma is good developer. Emma is a writer")
  pyramid(10)
  palindromeOrNot(424)
  listcreator(list1,list2)
  extractReverse(23456)


##01
def sum(value1, value2):
  if value1 * value2 < 1000:
    print(value1 * value2)
  else:
    print(value1 + value2)

##02
def iter():
  number = 0
  previousnumber = 0
  for i in range(10):
    print("Current Number",number,"Previous Number",previousnumber,"Sum:",(number + previousnumber))
    previousnumber = number
    number = number + 1

##03
def evenIndex(word):
  size = len(word)
  for i in range(0, size -1, 2):
    print(word[i])

##04
def removechars(word, amount):
  word = word[amount:]
  print(word)

##05
def checkFirstAndLast(array):
  firstChar = array[0]
  lastChar = array[len(array)-1]
  if firstChar == lastChar:
    print("true")
  else:
    print("false")

##06
def divisible5(list):
  for i in list:
    if i % 5 == 0:
      print(i)

##07
def countwords(word,string):
  print("Word", word , "appeared" , string.count(word) , "times.")

##08
def pyramid(number):
  for i in range(number + 1):
    for j in range(i):
      print (i, end=" ")
    print("\n")

##09
def palindromeOrNot(number):
  reversenum = str(number)[::-1]
  if number == int(reversenum):
    print(number,"is a palindrome")
  else:
    print(number, "is not a palindrome")

##10
def listcreator(list1,list2):
  newlist = []
  for i in list1: 
    if i % 2 != 0:
      newlist.append(i)
  for i in list2:
    if i % 2 == 0:
      newlist.append(i)
  print(newlist)

##11
def extractReverse(number):
  reversenumber = reversed(str(number))
  extracted = []
  for i in reversenumber:
    print(i,end = " ")

##12
##def calculatetax(income):
  







if __name__ == "__main__":
  main()