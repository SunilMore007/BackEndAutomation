
list=[1, 2.2, "Sunil", 4000 ]

print(list)

print(list[2]) #sunil
print(list[1:3 ])  #[2.2, 'Sunil']

list.insert(3, "More")
print(list) #[1, 2.2, 'Sunil', 'more', 4000]

print(list[-1]) # it gives the last element 4000

list.append("kavalapur") # Adding new element at the end
print(list)                #[1, 2.2, 'Sunil', 'More', 4000, 'kavalapur']

list[2]="SUNIL"   # to update
print(list)             #[1, 2.2, 'SUNIL', 'More', 4000, 'kavalapur']

del list[-1]   # To Delete the element from the list
print(list)     #[1, 2.2, 'SUNIL', 'More', 4000]

#============================ Tuples-same as list data type but immutable ======================================
list2=(1, 2, "Sunil", 4, 5, 6.7)
print(list2)       # (1, 2, 'Sunil', 4, 5, 6.7)

# Dictionary
dic ={1:" First Value" , 2: "Second value ", "third Key ": 3}
print(dic)
print(dic[1])
print(dic[2])
print(dic["third Key"])

