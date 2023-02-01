price = 49
txt = "The price is {} dollars"
print(txt.format(price))
price1 = 21
txt1 = "The price is {:.2f} dollars"
print(txt1.format(price1))
quantity = 3
itemno = 567
pr = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, pr))
q = 3
ino = 567
p = 49
myorder1 = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder1.format(q, ino, p))
age = 36
name = "John"
t = "His name is {1}. {1} is {0} years old."
print(t.format(age, name))
myo = "I have a {carname}, it is a {model}."
print(myo.format(carname = "Ford", model = "Mustang"))