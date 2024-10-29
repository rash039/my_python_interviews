str1 = 'GeeksforGeeks'
 
upper = lambda string: string.upper()
print(upper(str1))

#Output: ['Name1', '7.3', '6.9', '6.6', '6.6', '6.1', '6.4', '7.3']

# prime_numbers
#result = lambda(i, i if (i%2 == 0) ?  i: "")
#print(result(2))

# Find the first element that is greater than 5
greater_than_five = next((num for num in numbers if num > 5), None)

# EVEN numbers 
even_numbers = [num for num in range(1, 10) if num % 2 == 0 ]

print(even_numbers)

# Output: [2, 4, 6, 8]