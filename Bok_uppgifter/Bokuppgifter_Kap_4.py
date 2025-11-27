<<<<<<< HEAD
# Bokuppgifter kap 4
looping_list = [0, 'a', 'b', [1, 2, 3], ('Python', 'R', 
                                         'C', 'Java'), 55]
                
# Nr 1
for i in looping_list:
    print(i)

# Nr 2
# Enumerate
for (cnt, i) in enumerate(looping_list):
    print(cnt, i)    
    
# Nr 3  
for ix in range(21):
     if (ix % 5) == 0: # Printa bara det som är jämt delbart med 5
        print(ix)
        
# Nr 4
for_string = 'Python!' # Variant 1, iy ligger tecknet
for cnt,iy in enumerate(for_string):
    print(for_string[cnt], iy)

# Variant 2
for iy in for_string:
    print(iy)


# Nr 5
while_string = 'Is Awesome!'
i=0
while i<len(while_string):
    print(while_string[i])
    i=i+1
     
# Nr 6
ix = 0
while (ix<10):
    print(ix +1)
    ix=ix + 1

# Nr 7    
numbers = [10, 20, 34, 46, 55]
for ix in numbers:
    if (ix % 5 ==0):
        print(ix)
    
# Nr 8 Lägger in jämna tal i listan
my_list = []
for i in range(10):
    if i % 2 == 0:
        my_list.append(i)       
        
print(my_list)

# Nr 9

list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_new = []
for i in range(10):
    if (list_example[i]>=4 and list_example[i]<=8):
         list_new.append(list_example[i]*10)
        
print(list_new)

# Nr 10
# Skriver bara ut 1-10
for i in range(100):
    if i > 10:
        break
    print(i)
else:
=======
# Bokuppgifter kap 4
looping_list = [0, 'a', 'b', [1, 2, 3], ('Python', 'R', 
                                         'C', 'Java'), 55]
                
# Nr 1
for i in looping_list:
    print(i)

# Nr 2
# Enumerate
for (cnt, i) in enumerate(looping_list):
    print(cnt, i)    
    
# Nr 3  
for ix in range(21):
     if (ix % 5) == 0: # Printa bara det som är jämt delbart med 5
        print(ix)
        
# Nr 4
for_string = 'Python!' # Variant 1, iy ligger tecknet
for cnt,iy in enumerate(for_string):
    print(for_string[cnt], iy)

# Variant 2
for iy in for_string:
    print(iy)


# Nr 5
while_string = 'Is Awesome!'
i=0
while i<len(while_string):
    print(while_string[i])
    i=i+1
     
# Nr 6
ix = 0
while (ix<10):
    print(ix +1)
    ix=ix + 1

# Nr 7    
numbers = [10, 20, 34, 46, 55]
for ix in numbers:
    if (ix % 5 ==0):
        print(ix)
    
# Nr 8 Lägger in jämna tal i listan
my_list = []
for i in range(10):
    if i % 2 == 0:
        my_list.append(i)       
        
print(my_list)

# Nr 9

list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_new = []
for i in range(10):
    if (list_example[i]>=4 and list_example[i]<=8):
         list_new.append(list_example[i]*10)
        
print(list_new)

# Nr 10
# Skriver bara ut 1-10
for i in range(100):
    if i > 10:
        break
    print(i)
else:
>>>>>>> 0e12af3e5bea5bb0d4423cd5a917b131e52781fd
    print('done')