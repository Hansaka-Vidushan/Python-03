#Generators
def odd_numbers(limit):
    for i in range(0,limit):
        if i%2 ==1:
            yield i


x = odd_numbers(20)

for i in x:
    print("Loop" , i)

#Generators run 1 time
#Using Generators any time for import libraries

print(x)

