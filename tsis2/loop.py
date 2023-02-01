for y in 'birthday':
    print(y)
for c in 'birthday':
    print(c)
    if c=="t":
        break

num=[1,2,3,4,5]
for i in num:
    print(i)
for a in range(4):
    print(a)
    
for z in num:
    if z==4:
        break
    print(z)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)