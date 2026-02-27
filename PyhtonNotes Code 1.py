# way 1
l1 = [1,4,9,16,25,36,49,64,81,100]
# way 2 (traditional way)
sv=[]
for i in range(1,11):
  sv.append(i*i)
print(sv)
# way 3
l = [x**2 for x in range(1, 11)]
print(l1)
print(l)