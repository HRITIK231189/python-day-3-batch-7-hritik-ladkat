#!/usr/bin/env python
# coding: utf-8

# In[1]:


#You all are Pilots, you want to land a plane safely, so altitude required for landing a plane is 1000ft,it is less than tell pilot to land the plane, or it is more than that but less than 5000ft ask the pilot to"come down to 1000ft,else if it more than 5000ft ask the pilot to “go around and try again later

alt=int(input("enter the altitude you are at:"))
if alt<=1000:
    print("It is safe to land,you can land")
elif 1000<alt<5000:
    print("come down to 1000 ft")
else:
    print("go atound and try again please")
    


# In[2]:


# Python Program to print Prime Numbers from 1 to 200
 
for Number in range (1, 201):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')


# In[3]:


#python program to find the list of prime numbers in given number
def prime(lower,upper):
    for num in range(lower,upper+1):
        if num >1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                print(num)
print("program to find is prime numbers from given range")
print("enter the range [lower-upper]:")
lower=int(input())
upper=int(input())
print("the prime numbers are")
prime(lower,upper)


# In[ ]:




