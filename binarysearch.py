def binarysearch(list1,key):
    low = 0
    high = len(list1)-1
    found = False
    while low <= high and not found:
        mid=(low+high)//2
	 if key == list1[mid]:
	     found = True
	 elif key>list1[mid]:
	      low = mid+1
	 else:
	     high = mid-1
    if found == True:
      print("key found")
    else:
      print("key is not found")


list1 = [23,1,4,2,3]
list1.sort()
print(list1)
binarysearch(list1,key)