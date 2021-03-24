list=[]
num=int(input("enter the number of list elements"))
for pos in range(num):
   a = int(input("enter the num"))
   list.append(a)
print("unsorted list:",list)
for i in range(1,len(list)):
    pos=i-1
    
    while list[pos]>list[pos+1] and pos>=0:
        list[pos],list[pos+1]=list[pos+1],list[pos]
        pos-=1
    
    
    
print("sortedlist",list)