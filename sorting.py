data = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 21},
       {"name": "Nikhil", "age": 19}]

result = []
for records in data:
    if len(result)==0:
        result.append(records["age"])
        continue
    for elem in result:
        if elem < records["age"]:
            result.append(records["age"])
        elif (elem > records["age"]) and (records["age"] not in result):
            result =  [records["age"]] + result
print(result)

# # initializing list 
test_list = [1, 15, 3, 4, 5, 7]
  

for key in range(0, len(test_list)):
    for sub_key in range(key + 1, len(test_list)):
        # agar badha hai to age bhejo
        if test_list[key] > test_list[sub_key]:
            test_list[key] , test_list[sub_key] = test_list[sub_key], test_list[key]
print(test_list)


# Repeated 
arr = [12, 35, 1, 10, 34, 1]
outer_counter = 0
for each_element in arr:
    inner_counter = 0    
    for element in arr:
        if each_element < element :
             arr[inner_counter], arr[outer_counter] =  arr[outer_counter], arr[inner_counter]
        # elif each_element not in result:
        #     result += [each_element]
        inner_counter+=1
    outer_counter += 1
print(arr[len(arr)-2])
print("Second largest element{}".format(arr[-2:-1:]))

# directly print
print(arr[len(arr)-2])

