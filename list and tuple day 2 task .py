#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Calculate the cube of all numbers from 1 to a given number.

x = int(input("Enter a number"))
cube = x*x*x
print("Cube of {0} is {1} ".format(x, cube))


# In[12]:


#Use a loop to display elements from a given list present at odd index positions.

list = [98, 78, 12, 65, 77, 66, 587];   
print("Elements of given list present on odd position")
for i in range(0, len(list), 2):
    print(list[i]);


# In[24]:


#Use else block to display a message “Done” after successful execution of for loop.

for i in range (5):
    print(i)
    if i == 4:
        print("Done")
        break
else:
    print("uncompleted")


# In[27]:


#Print the following pattern.
for i in range(1, 6):
    for i in range(1, i+1):
        print(i, end=' ')
    print()


# In[28]:


#Write a Python program to remove duplicates from a list.

def remove_duplicates(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


# In[30]:


my_list = ['apple', 'banana', 'computer', 'apple', 'oxford', 'orange', 'computer']
new_list = remove_duplicates(my_list)
print(new_list)


# In[36]:


#Write a Python program to check if a list is empty or not.

list = []
if len(list) == 0:
    print("list is empty")
else:
    print("list is not empty")
    


# In[1]:


#Write a Python program to calculate the difference between the two lists.

list1 = [40, 20, 90, 50, 80]
list2 = [20, 10, 80, 40, 70]
difference = list(set(list1) - set(list2))
print(difference)


# In[2]:


#Write a Python program to find the second smallest and second largest  number in a list.

def find_second_smallest_largest(numbers):
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[1]
    second_largest = sorted_numbers[-2]
    return second_smallest, second_largest
numbers = [10, 2, 80, 4, 50, 7]
second_smallest, second_largest = find_second_smallest_largest(numbers)
print("Second smallest number:", second_smallest)
print("Second largest number:", second_largest)


# In[ ]:


#Write a Python program to check whether a list contains a sublist.

