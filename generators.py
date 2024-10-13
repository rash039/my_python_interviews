# list and generators
def even_numbers(limit):
    num = 0
    while num <= limit:
        if num % 2 == 0:
            yield num
        num += 1

# Usage
even_gen = even_numbers(10)
for even in even_gen:
    print(even)


#Output:
#0
#2
#4
#6
#8
#10

#yield allows the function to return values one at a time, without terminating the function.
#The generator keeps track of the state of the iteration, so you can iterate over the even numbers without storing them all in memory at once.

