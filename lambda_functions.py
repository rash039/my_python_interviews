str1 = 'GeeksforGeeks'
 
upper = lambda string: string.upper()
print(upper(str1))

#Replace all the elements in the list containing ‘\n’ with empty
l = ['Name1', '7.3', '6.9', '6.6', '6.6', '6.1', '6.4', '7.3\n']
#method1:
list(map(lambda x:x.strip(),l))
#Output: ['Name1', '7.3', '6.9', '6.6', '6.6', '6.1', '6.4', '7.3']