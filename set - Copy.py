collection = {1,2,3,2,"hello","world"}
collection.add(0)#to add element
collection.add("Rudra")
collection.remove("hello")#removes the element
collection.clear()#remove all the elements
print(collection.pop())#print the random values from set
print(collection)


#different way to create null set
Null = set()
print(type(Null))

#to take the union of two sets
collection2 = {7,9,6,5,}
mega = collection.union(collection2)
print(mega)

#to take the intersection of two set
inter = collection.intersection(collection2)
print(inter)