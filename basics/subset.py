a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

########### Write your code below ###############
res = a <=b # Is a subset of b?

########### Write your code above ###############
# Print True or False
print(res)


#unioon 

a = set([int(x) for x in input().strip().split()])
b = set([int(x) for x in input().strip().split()])

########### Write your code below ###############
st = a.union(b)# Union of a and b

########### Write your code above ###############

# Printing the size of the set which is the total number of elements in the set.
print(len(st))
