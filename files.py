import os

def main():
  file = open("test.txt","w", encoding="utf-8")
  file.write("Hello World")
  file.close()

  with open("test.txt","r", encoding="utf-8") as f:
    text = f.read()
    print(text)

  lines = ["\nPython on kivaa","\nKoodataan lisää\n"]
  with open("test.txt","a+", encoding="utf-8") as f:
    f.writelines(lines)

  with open("test.txt","r", encoding="utf-8") as f:
    print(f.read())
    f.seek(0)
    print(f.readline())

  os.remove("test.txt")

if __name__ == "__main__":
  main()