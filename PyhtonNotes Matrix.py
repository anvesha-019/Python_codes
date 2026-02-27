# To print the cube of the numbers from 0-n where n is given by the user using this comprehension
x = int(input("Enter the value: "))
l = [i**3 for i in range(0,x)]
print(l)

# Print 2D matrix 
md2 = [[i*j for j in range(0,5)] for i in range(0,5)]
print(md2)

# Print 3D matrix 
md2 = [[(i*j, i+j, i-j) for j in range(0,5)] for i in range(0,5)]
print(md2)

# Traditional way
for i in range(0,6):
  for j in range(0,6):
    print(i*j,i+j,i-j)

# Generate a 2D matrix using list comprehension and then swap it's even index elements with odd index elements
x = [[i*j for j in range(0,5)] for i in range(0,5)]
for i in range(0,4):
    for j in range(0,4):
       x[i][j], x[i+1][j+1] = x[i+1][j+1],x[i][j]
    print(x)