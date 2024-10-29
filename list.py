# import time

# class DemoAsyncMethod:

#     async def method_async():
#         time.sleep(10)


#     async def dependent_on_async():
#         response = await method_async()
#         print(response)



# ### 

# import requests

# response = ""
# max_retries = 0
# error_msg = ""
# while(max_retries):
#     try:
#         if max_retries == 3:
#             break
#         response = requests.get("https://google.com")
#         if response.status_code == 200:
#             data = response.text()
#     except Exception as e:
#         error_msg = str(e)

# print(error_msg)


# import itertools

# result = [data for data in range(0, 5)]
# for record in result:
#     print(record)
#     break

# for record in result:
#     print(record)
#     break




# result_object = (data for data in range(0, 5))

# for record in result_object:
#     # record1,,,
#     print(record)
#     break

# for record in result_object:
#     # record2,,,
#     print(record)
#     break

list1=[1,2,3,4,5]

list2=[4,5,7,8,9]

# list3=[1,2,3,7,8,9]

records_skip = [4,5]

# result = slice(records_skip, list1 + list2)

print(list1)


numbers = [1, 2, 3, 4, 5]

# Calculate the sum of all elements
total_sum = sum(numbers)

# Find the minimum and maximum values
min_value = min(numbers)
max_value = max(numbers)

### Querying Lists
#### Filtering Lists
##### You can filter lists using list comprehensions or the filter() function.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

##### Using list comprehension to filter even numbers
evens = [num for num in numbers if num % 2 == 0]

##### Using filter() with a lambda function
evens = list(filter(lambda x: x % 2 == 0, numbers))




### Searching Lists
####Search for elements or conditions in a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

##### Find the first element that is greater than 5
greater_than_five = next((num for num in numbers if num > 5), None)

##### Check if all elements are positive
all_positive = all(num > 0 for num in numbers)


def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

# Example usage
sentence = "I love coding in python"
print("The longest word is:", find_longest_word(sentence))
