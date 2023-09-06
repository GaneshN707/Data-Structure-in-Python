def enqueue(a):
    item = int(input("Enter Number To Enqueue: "))
    a.append(item)
def dequeue(a):
    if len(a)==0:
     print("Queue Underflow: ")
    else:
        item=a.pop(0)
        print("dDequeued item=" ,item)
def peek(a):
    if len (a) ==0:
        print("Queue Underflow: ")
    else:
        item = a[0]
        print("Peek item= ",item)
def display(a):
    if len(a)==0:
        print("Queue Underflow: ")
    else:
        for i in range(0,len(a)):
             print(a[i])

#__main()__
a=[]
while True:
    choice= int(input("\n1-Enqueue\n2-Dequeue\n3-Peek\n4-Display\n5-Exit\nEnter Number ->"))
    if choice==1:
        enqueue(a)
    elif choice==2:
        dequeue(a)
    elif choice==3:
        peek(a)
    elif choice==4:
        display(a)
    else:
        break
