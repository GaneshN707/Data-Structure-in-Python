def linear_Search(a,key,Size):
    flag=0
    for i in range (Size):
        if a[i]==key:
            flag=1
            break
    if flag==1:
        print(f"{key} Found at {i} Position")
    else:
        print(f"{key} Not Found..")

a=[]
Size=int(input("Enter Size Of The List"))
for i in range(Size):
    val=int(input("Enter Number"))
    a.append(val)
print(a)
key=int(input("Enter Number To Search"))
linear_Search(a,key,Size)



