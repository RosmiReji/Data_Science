a = [34,56,45,12,67]
print("Before sorting")
for i in a:
    print(i,end="")
    for i in range (0,len(a)):
        for  j in range(i+1,len(a)):
           if a[j] < a[i]:
               temp=a[j]
               a[j]=a[i]
               a[i]=temp
               print("After sorting")
               for i in a:
                    print(i,end="")