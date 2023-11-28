#!/usr/bin/env python
# coding: utf-8

# In[9]:


#dictionary from https://norvig.com/



from collections import Counter 

n = input("What's the minimal length of a legal word:")

#read the files
files = list()
#i = 0
with open("count_1w.txt") as file:
        for item in file:
            
            #use this part to limit to the first 5k of dictionary
            #i+=1
            #
            #if i >= 5000:
            #    break
            
            #the list is already sorted by their popularity so we don't need to sort it later
            word = item.rstrip('\n')
            word = word.split('\t')[0]
            if len(word) >= int(n):
                files.append(word)
                
#counting using Counter            
items = []
for item in files:
    c = Counter(item)
    length = len(item)
    items.append([item,c,length])
    
#main test loop
while(True):
    required = input("Enter all required letters:(enter any number if you want to leave)")
    if any(char.isdigit() for char in required):
        break
    
    #count the input letters
    d = Counter(required)
    #print(d)
    
    #character test
    def test_if_bad(item,d):
        for i in item[1]:
            if d.get(i) == None or d.get(i) < item[1][i]:
                return True

        return False

    _len = sum(d.values())
    res = []
    for item in items:
        if item[2] <= _len: # too long
            #res.append(item)

            if test_if_bad(item,d): # checks for letters count
                continue

            else:
                res.append(item) # ok we good 
        else:
            continue

    for word in res:
        print(word[0], end="\t")


# In[ ]:




