def insertion_sort(list):
    for index in range(1,len(list)):
        current_value = list[index]
        position = index
        while(position > 0 and list[position-1] > current_value):
            list[position] = list[position-1]
            position = position-1
        list[position] = current_value
        print("list after insertion sort",list)            
            
list = []
n = int(input("Enter the size of list"))
for i in range(n):
    list.append(int(input()))
insertion_sort(list)
