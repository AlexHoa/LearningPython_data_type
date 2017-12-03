#!usr/local/bin/python3.6
'''Create a list of tuples where the first value in the tuple is the temperature in Celcius and the second in farenheit
take a look at the range function
Same thing but place swapped. From 0 to 100 farenheit
Celcius = (Farenheit -32)* 5/9
Farenheit = Celcius * 9/5 +32
'''

# creation of the list comprehension : (C°, F°)
r = range(21)
l = [(i,(i*9/5 +32)) for i in r]
print(l)
print("\n")

#swapped
lswapped=(l[1], l[0])

# creation of the list comprehension: (F°, C°)
r2 = range(101)
l2 = [(i, (i-32)*5/9) for i in r2]
print(l2)

