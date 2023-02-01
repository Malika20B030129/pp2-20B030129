print(500 > 400)

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"),bool(5))
print(bool(0), bool({}))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True
print(myFunction())

def Func() :
  return True
if Func():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))

y='hi'
print(isinstance(y, int))