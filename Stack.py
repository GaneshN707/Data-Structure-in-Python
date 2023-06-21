def push(a, val):
    a.append(val)
    print("Element Pushed Successfully")
def pop(a):
    val = a.pop()
    print("Popped Item=",val)
def peek(a):
    index = len(a)-1
    print("Peek Element",a[index])
def display(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])

a = []
while True:
    choice = int(input(" 1 - Push \n 2 - Pop \n 3 - Peek \n 4 - display\n 5 - Exit \nEnter Your Choice: "))
    if choice == 1:
        val = int(input("Enter Number To Push"))
        push(a,val)
    elif choice == 2:
        if len(a)== 0:
           print("Empty Stack")
        else:
             pop(a)
    elif choice == 3:
        if len(a) == 0:
            print("Empty Stack")
        else:
            peek(a)
    elif choice == 4:
        if len(a) == 0:
            print("Empty Stack")
        else:
            display(a)
    else:
        break



