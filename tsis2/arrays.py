num=[10,45,66,93,700]
print(num[0],len(num),num.index(45))
for i in num:
    print(i)
num.append(99)
num.pop(3)
num.insert(1,25)
for i in num:
    if i==66:
        num.remove(i)
print(num)
num.reverse()
print(num)
