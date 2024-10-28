# Why are Python Strings Immutable?

Strings in Python are “immutable” which means they can not be changed after they are created. 

Some other immutable data types are integers, float, boolean, etc. 


Input:  name_1 = "Aarun" 
             name_1[0] = 'T' 
Output: TypeError: 'str' object does not support item assignment
Explanation: We cannot update the string after declaring it means once an immutable the objects instantiated, its value cannot be changed

# Other working
s = 'Rashid'
s = 'Alam'
print(s)
#O/P: 'Alam'

#1. String Slicing and Reassembling:
name_1 = "Aarun"

name_2 = "T" + name_1[1:]

print("name_1 = ", name_1, "and name_2 = ", name_2)

#name_1 =  Aarun and name_2 =  Tarun

