
print("Hello")

x= 5
y=6.5
isRaining = True
name="Eshan Ahmed"
print(x+y)
print(type(name))

#type casting
z=str(y)
print(z)

c = float(x)
print(c)
print(type(c))

#string formatting
name = "Simi"
age=15


print('{},{},{}'.format('1','2',5))
print('My name is {name} and my age is {age}'.format(name=name,age=age))



s= "I am Eshan"

print(s.upper())
print(s.find('E'))



animals = ["tiger","lion","deer","monkey"]

animals.append("cow")
print(animals)
#print(len(animals))

#animals.pop(1)
#print(animals)

#animals.sort()
print(animals[2].isnumeric())