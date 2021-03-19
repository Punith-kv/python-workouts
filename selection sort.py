def selection_sort(a):
      for i in range(len(a)):
           min_pos = i
           for j in range(i+1,len(a)):
               if a[j] < a[min_pos] :
                    min_pos = j
           a[i],a[min_pos]  = a[min_pos],a[i]
           

a = []
n = int(input("enter the size"))
for i in range(n):
    a.append(int(input()))
selection_sort(a)
print("after insertion",a)

