a = int(input())
b = int(input())
c = int(input())
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if c>a and b<a:
    print('yes')
else:
    print('no')

if not a<b:
    print('yes')
else:
    print('no')

if a>b or a>c:
    print('yes')
if a>10:
    if a>20:
        print('above 20')
    else:
        print('not above 20')
else:
    print('less than 10')
if b<a:
    pass