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