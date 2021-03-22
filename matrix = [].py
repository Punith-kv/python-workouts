matrix = [] 
print("Enter the entries rowwise:") 
R=int(input("enter row"))
C=int(input("Enter coloums")) 
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 